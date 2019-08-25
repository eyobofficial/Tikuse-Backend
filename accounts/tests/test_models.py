from django.test import TestCase

from .factories import HostFactory, GuestFactory


class HostProfileModelTests(TestCase):
    """
    Tests for `HostProfile` model methods
    """

    def setUp(self):
        self.user = HostFactory(phone_number='+251911000000')
        self.user.host.full_name = 'John Doe'

    def test_get_full_name_method(self):
        """
        Ensure `get_full_name` method returns the full name of the `host`.
        """
        self.assertEqual(self.user.host.get_full_name(), 'John Doe')

    def test_get_first_name(self):
        """
        Ensure `get_first_name` method returns the first name of the `host`.
        """
        self.assertEqual(self.user.host.get_first_name(), 'John')


class GuestProfileModelTests(TestCase):
    """
    Tests for `GuestProfile` model methods
    """

    def setUp(self):
        self.user = GuestFactory(phone_number='+251911000000')
        self.user.guest.full_name = 'John Doe'

    def test_get_full_name_method(self):
        """
        Ensure `get_full_name` method returns the full name of the `guest`.
        """
        self.assertEqual(self.user.guest.get_full_name(), 'John Doe')

    def test_get_first_name(self):
        """
        Ensure `get_first_name` method returns the first name of the `guest`.
        """
        self.assertEqual(self.user.guest.get_first_name(), 'John')
