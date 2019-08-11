import africastalking

from django.conf import settings
from django.db import transaction

from shared.constants import LANG_ENGLISH
from shared.models import SMS


class BaseSMS:
    subject = None
    message = {}
    recipient = None
    _sender = None
    _sms = None
    _provider = None
    _sms_type = None

    def _save(self, lang):
        """
        Persist SMS to database.
        """
        return SMS.objects.create(
            subject=self.subject,
            provider=self._provider,
            type=self._sms_type,
            sender=self._sender,
            recipient=self.recipient,
            message=self.message[lang]
        )


class AfricasTalking(BaseSMS):
    _provider = SMS.AFRICASTALKING
    _sender = settings.AFRICASTALKING_SHORT_CODE
    _api_username = settings.AFRICASTALKING_API_USERNAME
    _api_key = settings.AFRICASTALKING_API_KEY

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_sdk()

    def _init_sdk(self):
        """
        Initialize the SDK
        """
        africastalking.initialize(self._api_username, self._api_key)
        self._sms = africastalking.SMS

    @transaction.atomic
    def send(self, **kwargs):
        """
        Send SMS to the recipients list
        """
        lang = kwargs.get('lang')
        if not lang:
            lang = LANG_ENGLISH  # English default langugae
        message = self.message[lang]
        recipients = [self.recipient.phone_number.as_e164]
        sender = self._sender

        try:
            self._sms.send(message, recipients, sender)
            self._save(lang)
        except Exception as e:
            raise ValueError(e)


class NotificationMixin:
    _sms_type = SMS.NOTIFICATION


class ReminderMixin:
    _sms_type = SMS.REMINDER


class AdMixin:
    _sms_type = SMS.ADVERTISEMENT
