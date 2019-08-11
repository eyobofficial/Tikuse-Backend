from shared.sms.base import NotificationMixin

from shared.constants import LANG_AMHARIC, LANG_ENGLISH

from .base import BaseAccountSMS
from .templates import HOST_SIGNUP_EN, HOST_SIGNUP_AM


class HostSignupNotificationSMS(BaseAccountSMS, NotificationMixin):
    """
    SMS sent when a new `Host` is registered.
    """
    subject = 'Host Registration'

    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        first_name = self.recipient.get_first_name()
        self.message[LANG_ENGLISH] = HOST_SIGNUP_EN.format(first_name)
        self.message[LANG_AMHARIC] = HOST_SIGNUP_AM.format(first_name)
