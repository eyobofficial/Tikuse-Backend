from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser, GuestProfile, HostProfile


User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a user profile when a new user instance is created.
    """
    if created and instance.role == CustomUser.GUEST:
        GuestProfile.objects.create(user=instance)
    elif created and instance.role == CustomUser.HOST:
        HostProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Update a user profile when a new user instance is updated.
    """
    if instance.role == CustomUser.GUEST:
        guest, is_created = GuestProfile.objects.get_or_create(user=instance)
        if not is_created:
            guest.save()

    elif instance.role == CustomUser.HOST:
        host, is_created = HostProfile.objects.get_or_create(user=instance)
        if not is_created:
            host.save()
