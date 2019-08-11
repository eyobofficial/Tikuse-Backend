from shared.sms.base import NotificationMixin, AfricasTalking


class BaseAccountSMS(NotificationMixin, AfricasTalking):
    """
    SMS sent when a new `Host` is registered.
    """

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.recipient = user
