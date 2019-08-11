import mock

from django.test import TestCase

from accounts.sms.notifications import HostSignupNotificationSMS
from .factories import HostFactory


class HostSignupNotificationSMSTests(TestCase):
    """
    Tests `HostSignupNotificationSMS`
    """

    def setUp(self):
        self.host = HostFactory(phone_number='+251911000000')

    @mock.patch('accounts.sms.notifications.HostSignupNotificationSMS.send')
    def test_sms_with_default_values(self, mock_sms):
        """
        Ensure SMS is properly sent with the default values.
        """
        email = HostSignupNotificationSMS(self.host)
        email.send()

        # Assertions
        self.assertTrue(mock_sms.called)
        self.assertEqual(email._sms_type, 'NOTIFICATION')
