from django.contrib import admin

from shared.admin import CustomURLModelAdmin

from .models import CustomUser
from .views import HostSignupNotificationEN, HostSignupNotificationAM


@admin.register(CustomUser)
class CustomUserAdmin(CustomURLModelAdmin):
    exclude = ('first_name', 'last_name', 'email')
    list_display = (
        'public_id',
        'username',
        'phone_number',
        'email',
        'full_name',
        'role',
        'is_active',
        'is_staff',
        'is_superuser',
        'last_login'
    )
    list_display_link = ('username', 'phone_number')
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'phone_number', 'full_name')
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
