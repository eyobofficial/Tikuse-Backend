from django.test import TestCase

from profiles.models import Profile
from .factories import UserFactory, GuestFactory, HostFactory


class CreateUserProfileTests(TestCase):
    """
    Tests for `create_user_profile` signal
    """

    def test_creating_host_user_profile(self):
        """
        Ensure creating a new HOST also creates an associated
        profile
        """
        user = GuestFactory()
        self.assertEqual(Profile.objects.filter(user=user).count(), 1)

    def test_creating_guest_user_profile(self):
        """
        Ensure creating a new GUEST also creates an associated
        profile
        """
        user = HostFactory()
        self.assertEqual(Profile.objects.filter(user=user).count(), 1)

    def test_creating_user_with_no_role(self):
        """
        Ensure creating a new user with ROLE attribue does not creates
        an associated profile
        """
        user = UserFactory()
        self.assertEqual(Profile.objects.filter(user=user).count(), 0)
