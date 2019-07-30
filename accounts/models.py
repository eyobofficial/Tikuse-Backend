from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from shared.utilities.commons import generate_public_id


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    public_id = models.CharField(
        max_length=12,
        unique=True,
        editable=False,
        default=generate_public_id
    )
    phone_number = PhoneNumberField(unique=True)

    def __str__(self):
        return self.username


class Profile(models.Model):

    # User types
    HOST = 'HOST'
    GUEST = 'GUEST'

    TYPE_CHOICES = (
        (HOST, 'Host'),
        (GUEST, 'Guest')
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    full_name = models.CharField(max_length=120)
    type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    is_activated = models.BooleanField('activated', default=False)

    def __str__(self):
        return self.full_name
