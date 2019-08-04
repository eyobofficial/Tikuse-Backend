from django.contrib import admin

from .models import GuestProfile, HostProfile, HostPhoto


@admin.register(GuestProfile)
class GuestProfileAdmin(admin.ModelAdmin):
    list_display = ('public_id', 'user', 'created_at', 'updated_at')


@admin.register(HostProfile)
class HostProfileAdmin(admin.ModelAdmin):
    list_display = (
        'public_id',
        'user',
        'is_activated',
        'created_at',
        'updated_at'
    )
    list_filter = ('is_activated', )


@admin.register(HostPhoto)
class HostPhotoAdmin(admin.ModelAdmin):
    list_display = ('public_id', 'profile', 'title', 'created_at')
