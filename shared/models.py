from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class SMS(models.Model):
    # SMS Providers
    AFRICASTALKING = 'AFRICAS_TALKING'
    TWILIO = 'TWILIO'

    provider_choices = (
        (AFRICASTALKING, 'Africas Talking'),
        (TWILIO, 'Twilio')
    )

    # SMS message type
    NOTIFICATION = 'NOTIFICATION'
    REMINDER = 'REMINDER'
    ADVERTISEMENT = 'ADVERTISEMENT'

    type_choices = (
        (NOTIFICATION, 'Notification'),
        (REMINDER, 'Reminder'),
        (ADVERTISEMENT, 'Advertisement')
    )

    subject = models.CharField(max_length=120)
    provider = models.CharField(
        max_length=30,
        choices=provider_choices,
        default=AFRICASTALKING
    )
    type = models.CharField(
        max_length=30,
        choices=type_choices,
        default=NOTIFICATION
    )
    sender = models.CharField(max_length=30, blank=True)
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-sent_at', )
        verbose_name = 'SMS'
        verbose_name_plural = 'SMS'

    def __str__(self):
        return f'{self.subject} - <{self.recipient.username}>'
