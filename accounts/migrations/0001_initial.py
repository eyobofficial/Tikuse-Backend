# Generated by Django 2.2.4 on 2019-08-13 19:36

import accounts.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
import shared.utilities.commons
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('public_id', models.CharField(default=shared.utilities.commons.generate_public_id, editable=False, max_length=12, unique=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('full_name', models.CharField(max_length=120)),
                ('role', models.CharField(blank=True, choices=[('HOST', 'Host'), ('GUEST', 'Guest')], max_length=5, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='HostProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('public_id', models.CharField(default=shared.utilities.commons.generate_public_id, editable=False, max_length=12, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to=accounts.models.hash_location)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('about', models.TextField(blank=True)),
                ('address', models.TextField(blank=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('is_activated', models.BooleanField(default=False, verbose_name='activated')),
                ('cover_picture', models.ImageField(blank=True, null=True, upload_to=accounts.models.hash_location)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='host', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_related_name': 'host',
            },
        ),
        migrations.CreateModel(
            name='GuestProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('public_id', models.CharField(default=shared.utilities.commons.generate_public_id, editable=False, max_length=12, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to=accounts.models.hash_location)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='guest', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_related_name': 'guest',
            },
        ),
        migrations.CreateModel(
            name='HostPhoto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('public_id', models.CharField(default=shared.utilities.commons.generate_public_id, editable=False, max_length=12, unique=True)),
                ('photo', models.ImageField(upload_to=accounts.models.hash_location)),
                ('title', models.CharField(blank=True, max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='accounts.HostProfile')),
            ],
            options={
                'order_with_respect_to': 'profile',
            },
        ),
    ]
