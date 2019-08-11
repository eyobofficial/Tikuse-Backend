from django.contrib import admin
from django.conf.urls import url

from .models import SMS


class CustomURLModelAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        additional_urls = []

        for custom_url in self.custom_urls:
            view = custom_url['view'].as_view()
            custom_url['view'] = self.admin_site.admin_view(view)
            additional_urls.append(url(**custom_url))

        return additional_urls + urls


@admin.register(SMS)
class SMSMessageAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'recipient',
        'type',
        'provider',
        'sent_at'
    )
    readonly_fields = (
        'subject',
        'provider',
        'type',
        'sender',
        'recipient',
        'message',
        'sent_at'
    )
    list_filter = ('type', 'provider')
    search_fields = ('subject', 'message')
