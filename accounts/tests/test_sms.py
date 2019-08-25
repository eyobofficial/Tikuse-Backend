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
        self.host.host.full_name = 'John Doe'

    @mock.patch('accounts.sms.notifications.HostSignupNotificationSMS.send')
    def test_sms_with_default_values(self, mock_sms):
        """
        Ensure SMS is properly sent with the default values.
        """
        sms = HostSignupNotificationSMS(self.host)
        sms.send()

        # Assertions
        self.assertTrue(mock_sms.called)
        self.assertEqual(sms._sms_type, 'NOTIFICATION')
