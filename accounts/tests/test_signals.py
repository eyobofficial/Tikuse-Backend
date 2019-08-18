from django.test import TestCase

from accounts.models import GuestProfile, HostProfile
from .factories import UserFactory, GuestFactory, HostFactory


class CreateUserProfileTests(TestCase):
    """
    Tests for `create_user_profile` signal
    """

    def setUp(self):
        self.valid_phone_number = '+251911000000'

    def test_creating_host_user_profile(self):
        """
        Ensure creating a new HOST also creates an associated
        HostProfile instance
        """
        user = GuestFactory(phone_number=self.valid_phone_number)
        self.assertEqual(GuestProfile.objects.filter(user=user).count(), 1)

    def test_creating_guest_user_profile(self):
        """
        Ensure creating a new GUEST also creates an associated
        GuestProfile instance
        """
        user = HostFactory(phone_number=self.valid_phone_number)
        self.assertEqual(HostProfile.objects.filter(user=user).count(), 1)

    def test_creating_user_with_no_role(self):
        """
        Ensure creating a new user with ROLE attribue does not creates
        an associated profile
        """
        user = UserFactory(phone_number=self.valid_phone_number)
        self.assertEqual(GuestProfile.objects.filter(user=user).count(), 0)
        self.assertEqual(HostProfile.objects.filter(user=user).count(), 0)
