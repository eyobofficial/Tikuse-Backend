from django.contrib import admin

from shared.admin import CustomURLModelAdmin

from .models import CustomUser, GuestProfile, HostProfile, HostPhoto
from .views import HostSignupNotificationEN, HostSignupNotificationAM


@admin.register(CustomUser)
class CustomUserAdmin(CustomURLModelAdmin):
    exclude = ('first_name', 'last_name', 'email')
    list_display = (
        'public_id',
        'username',
        'phone_number',
        'email',
        'role',
        'is_active',
        'is_staff',
        'is_superuser',
        'last_login'
    )
    list_display_link = ('username', 'phone_number')
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'phone_number')
    custom_urls = [
        {
            'regex': r'^(?P<pk>.+)/send-host-signup-notification-en/$',
            'view': HostSignupNotificationEN,
            'name': 'send-host-signup-notification-en'
        },
        {
            'regex': r'^(?P<pk>.+)/send-host-signup-notification-am/$',
            'view': HostSignupNotificationAM,
            'name': 'send-host-signup-notification-am'
        },
    ]


@admin.register(GuestProfile)
class GuestProfileAdmin(admin.ModelAdmin):
    list_display = ('public_id', 'user', 'created_at', 'updated_at')


class HostPhotoInline(admin.TabularInline):
    model = HostPhoto
    extra = 1


@admin.register(HostProfile)
class HostProfileAdmin(admin.ModelAdmin):
    list_display = (
        'public_id',
        'user',
        'full_name',
        'is_activated',
        'created_at',
        'updated_at'
    )
    list_filter = ('is_activated', )
    inlines = (HostPhotoInline, )
