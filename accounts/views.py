from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response

from rest_framework_jwt.settings import api_settings

from .models import CustomUser
from .serializers import UserSerializer
from .utilities import jwt_response_payload_handler


User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class HostSignUpAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # Validate serialized data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Create new user
        user = serializer.save()
        user.role = CustomUser.HOST
        user.save()

        # Generate JWT token
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        # Include user data along with token
        data = jwt_response_payload_handler(token, user, request)
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
