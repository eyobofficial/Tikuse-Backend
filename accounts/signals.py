from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from profiles.models import Profile


User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a user profile when a new user instance is created.
    """
    if created and instance.role:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Update a user profile when a new user instance is updated.
    """
    try:
        profile = Profile.objects.get(user=instance)
        profile.save()
    except Profile.DoesNotExist:
        pass
