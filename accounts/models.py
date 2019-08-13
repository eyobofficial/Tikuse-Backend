from uuid import uuid4
from unicodedata import normalize

from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from shared.utilities.commons import generate_public_id


def hash_location(instance, filename):
    """
    Location for saving profile files
    """
    filename = normalize('NFKD', filename).encode('ascii', 'ignore')
    filename = filename.decode('UTF-8')
    return f'uploads/accounts/{uuid4()}/{filename}'


class CustomUser(AbstractUser):

    # User types
    HOST = 'HOST'
    GUEST = 'GUEST'

    TYPE_CHOICES = (
        (HOST, 'Host'),
        (GUEST, 'Guest')
    )

    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    public_id = models.CharField(
        max_length=12,
        unique=True,
        editable=False,
        default=generate_public_id
    )
    phone_number = PhoneNumberField(unique=True)
    full_name = models.CharField(max_length=120)
    role = models.CharField(
        max_length=5,
        choices=TYPE_CHOICES,
        blank=True, null=True
    )

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.full_name

    def get_first_name(self):
        return self.full_name.split()[0].title()


class BaseProfile(models.Model):
    """
    Abstract Base Profile Model Class.
    """
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4
    )
    public_id = models.CharField(
        max_length=12,
        unique=True,
        editable=False,
        default=generate_public_id
    )
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE
    )
    email = models.EmailField(blank=True)
    profile_picture = models.ImageField(
        upload_to=hash_location,
        null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class GuestProfile(BaseProfile):
    pass

    class Meta:
        default_related_name = 'guest'


class HostProfile(BaseProfile):
    about = models.TextField(blank=True)
    address = models.TextField(blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    is_activated = models.BooleanField('activated', default=False)
    cover_picture = models.ImageField(
        upload_to=hash_location,
        null=True, blank=True
    )

    class Meta:
        default_related_name = 'host'

    def __str__(self):
        return self.user.username


class HostPhoto(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4
    )
    public_id = models.CharField(
        max_length=12,
        unique=True,
        editable=False,
        default=generate_public_id
    )
    profile = models.ForeignKey(
        HostProfile,
        on_delete=models.CASCADE,
        related_name='photos'
    )
    photo = models.ImageField(upload_to=hash_location)
    title = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        order_with_respect_to = 'profile'

    def __str__(self):
        return self.title
