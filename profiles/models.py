import uuid
from unicodedata import normalize

from django.contrib.auth import get_user_model
from django.db import models

from shared.utilities.commons import generate_public_id

User = get_user_model()


def hash_location(instance, filename):
    """
    Location for saving profile files
    """
    filename = normalize('NFKD', filename).encode('ascii', 'ignore')
    filename = filename.decode('UTF-8')
    return f'uploads/profiles/{uuid.uuid4()}/{filename}'


class BaseProfile(models.Model):
    """
    Abstract Base Profile Model Class.
    """
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    public_id = models.CharField(
        max_length=12,
        unique=True,
        editable=False,
        default=generate_public_id
    )
    user = models.OneToOneField(
        User,
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
        default=uuid.uuid4
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
