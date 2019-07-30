from django.contrib import admin

from .models import CustomUser, Profile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'public_id',
        'username',
        'phone_number',
        'email',
        'is_active',
        'is_staff',
        'is_superuser',
        'last_login'
    )
    list_display_link = ('username', 'phone_number')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'phone_number')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name')
    list_display_link = ('user', 'full_name')
    search_fields = ('full_name', )
