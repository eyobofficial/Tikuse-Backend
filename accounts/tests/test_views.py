import mock

from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .factories import HostFactory
from accounts.models import CustomUser


User = get_user_model()


class HostSignUpAPIViewTests(APITestCase):
    """
    Tests for `host-signup` endpoint
    """

    def setUp(self):
        self.url = reverse('v1-accounts:host-signup')

    def test_endpoint_with_GET_request(self):
        """
        Ensure GET http request is not allowed.
        """
        response = self.client.get(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

    @mock.patch('accounts.sms.notifications.HostSignupNotificationSMS.send')
    def test_endpoint_with_POST_request_and_valid_data(self, mock_sms):
        """
        Ensure that a POST request with:
            - username
            - password
            - full_name
            - phone_number
        creates a new Host user and returns a JWT token with user data.
        """
        payload = {
            'username': 'testuser',
            'password': 'Passw0rd1234',
            'full_name': 'Test User',
            'phone_number': '+251911000000'
        }
        response = self.client.post(self.url, payload, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().role, CustomUser.HOST)
        self.assertTrue('token' in response.json())
        self.assertTrue('id' in response.json())
        self.assertTrue('username' in response.json())
        self.assertTrue('full_name' in response.json())
        self.assertTrue('phone_number' in response.json())
        self.assertTrue('role' in response.json())
        self.assertTrue('last_login' in response.json())
        self.assertTrue('date_joined' in response.json())
        self.assertEqual(mock_sms.call_count, 2)

    def test_endpoint_with_POST_request_without_a_username(self):
        """
        Ensuer that a POST request without a `username` data does not
        creates a new user.
        """
        payload = {
            'password': 'Passw0rd1234',
            'full_name': 'Test User',
            'phone_number': '+251911000000'
        }
        response = self.client.post(self.url, payload, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

    def test_endpoint_with_POST_request_without_a_password(self):
        """
        Ensuer that a POST request without a `password` data does not
        creates a new user.
        """
        payload = {
            'username': 'testuser',
            'full_name': 'Test User',
            'phone_number': '+251911000000'
        }
        response = self.client.post(self.url, payload, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

    def test_endpoint_with_POST_request_without_a_full_name(self):
        """
        Ensuer that a POST request without a `full_name` data does not
        creates a new user.
        """
        payload = {
            'username': 'testuser',
            'password': 'Passw0rd1234',
            'phone_number': '+251911000000'
        }
        response = self.client.post(self.url, payload, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

    def test_endpoint_with_POST_request_without_a_phone_number(self):
        """
        Ensuer that a POST request without a `phone_number` data does not
        creates a new user.
        """
        payload = {
            'username': 'testuser',
            'password': 'Passw0rd1234',
            'full_name': 'Test User'
        }
        response = self.client.post(self.url, payload, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

    def test_endpoint_with_POST_request_with_invalid_phone_number(self):
        """
        Ensuer that a POST request without a invalid phone number data
        does not creates a new user.
        """
        payload = {
            'username': 'testuser',
            'password': 'Passw0rd1234',
            'full_name': 'Test User',
            'phone_number': '1234'
        }
        response = self.client.post(self.url, payload, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

    def test_endpoint_with_POST_request_and_existing_username(self):
        """
        Ensuer that a POST request with an existing `username` data
        does not creates a new user.
        """
        HostFactory(username='testuser', password='+251911111111')
        payload = {
            'username': 'testuser',
            'password': 'Passw0rd1234',
            'full_name': 'Test User',
            'phone_number': '+251911000000'
        }
        response = self.client.post(self.url, payload, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_endpoint_with_POST_request_and_existing_phone_number(self):
        """
        Ensuer that a POST request with an existing `phone_number` data
        does not creates a new user.
        """
        HostFactory(username='otheruser', phone_number='+251911000000')
        payload = {
            'username': 'testuser',
            'password': 'Passw0rd1234',
            'full_name': 'Test User',
            'phone_number': '+251911000000',
            'role': 'HOST'
        }
        response = self.client.post(self.url, payload, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)


class LoginEndpointTests(APITestCase):
    """
    Tests for `login` API endpoint
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='Passw0rd1234',
            full_name='Test User',
            phone_number='+251911000000'
        )
        self.url = reverse('v1-accounts:login')

    def test_endpoint_with_GET_request(self):
        """
        Ensure GET http request is not allowed.
        """
        response = self.client.get(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_endpoint_with_valid_username_and_password(self):
        """
        Ensure POST http request with valid `username` & `password`,
        returns a token key.
        """
        payload = {
            'username': 'testuser',
            'password': 'Passw0rd1234'
        }
        response = self.client.post(self.url, payload, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.json())
        self.assertTrue('id' in response.json())
        self.assertTrue('username' in response.json())
        self.assertTrue('full_name' in response.json())
        self.assertTrue('phone_number' in response.json())
        self.assertTrue('role' in response.json())
        self.assertTrue('last_login' in response.json())
        self.assertTrue('date_joined' in response.json())

    def test_endpoint_with_valid_phone_number_and_password(self):
        """
        Ensure POST http request with valid `phone_number` & `password`,
        returns a token key.
        """
        payload = {
            'username': '+251911000000',
            'password': 'Passw0rd1234'
        }
        response = self.client.post(self.url, payload, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.json())
        self.assertTrue('id' in response.json())
        self.assertTrue('username' in response.json())
        self.assertTrue('full_name' in response.json())
        self.assertTrue('phone_number' in response.json())
        self.assertTrue('role' in response.json())
        self.assertTrue('last_login' in response.json())
        self.assertTrue('date_joined' in response.json())

    def test_endpoint_with_invalid_username_and_password(self):
        """
        Ensure POST http request with invalid `username` & `password`,
        does not return a token key.
        """
        payload = {
            'username': 'invaliduser',
            'password': 'Passw0rd1234'
        }
        response = self.client.post(self.url, payload, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse('token' in response.json())

    def test_endpoint_with_invalid_phone_number_and_password(self):
        """
        Ensure POST http request with invalid `phone_number` & `password`,
        does not return a token key.
        """
        payload = {
            'username': '+251911000001',
            'password': 'Passw0rd1234'
        }
        response = self.client.post(self.url, payload, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse('token' in response.json())
