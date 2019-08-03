from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
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
