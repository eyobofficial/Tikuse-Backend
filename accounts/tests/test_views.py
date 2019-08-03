from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .factories import HostFactory


User = get_user_model()


class SignUpAPIViewTests(APITestCase):
    """
    Tests for `SignUpAPIView` class
    """

    def setUp(self):
        self.url = reverse('v1-accounts:signup')

    def test_endpoint_with_GET_request(self):
        """
        Ensure GET http request is not allowed.
        """
        response = self.client.get(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_endpoint_with_POST_request_and_valid_data(self):
        """
        Ensure that a POST request with:
            - username
            - password
            - full_name
            - phone_number
            - role
        creates a new user and returns an authentication key.
        """
        payload = {
            'username': 'testuser',
            'password': 'Passsword1234',
            'full_name': 'Test User',
            'phone_number': '+251911000000',
            'role': 'HOST'
        }
        response = self.client.post(self.url, payload, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertTrue('key' in response.json())

    def test_endpoint_with_POST_request_without_a_username(self):
        """
        Ensuer that a POST request without a `username` data does not
        creates a new user.
        """
        payload = {
            'password': 'Passsword1234',
            'full_name': 'Test User',
            'phone_number': '+251911000000',
            'role': 'HOST'
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
            'phone_number': '+251911000000',
            'role': 'HOST'
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
            'password': 'Passsword1234',
            'phone_number': '+251911000000',
            'role': 'HOST'
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
            'password': 'Passsword1234',
            'full_name': 'Test User',
            'role': 'HOST'
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
            'password': 'Passsword1234',
            'full_name': 'Test User',
            'phone_number': '1234',
            'role': 'HOST'
        }
        response = self.client.post(self.url, payload, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

    def test_endpoint_with_POST_request_without_a_role(self):
        """
        Ensuer that a POST request without a `role` data does not
        creates a new user.
        """
        payload = {
            'username': 'testuser',
            'password': 'Passsword1234',
            'full_name': 'Test User',
            'phone_number': '+251911000000'
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
        HostFactory(username='testuser')  # Existing username
        payload = {
            'username': 'testuser',
            'password': 'Passsword1234',
            'full_name': 'Test User',
            'phone_number': '+251911000000',
            'role': 'HOST'
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
        HostFactory(phone_number='+251911000000')  # Existing username
        payload = {
            'username': 'testuser',
            'password': 'Passsword1234',
            'full_name': 'Test User',
            'phone_number': '+251911000000',
            'role': 'HOST'
        }
        response = self.client.post(self.url, payload, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
