from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework_jwt.settings import api_settings

from shared.constants import LANG_AMHARIC, LANG_ENGLISH
from shared.views import BaseSMSView

from .models import CustomUser
from .serializers import HostSerializer
from .sms.notifications import HostSignupNotificationSMS
from .utilities import jwt_response_payload_handler


User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class HostSignUpAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = HostSerializer

    def create(self, request, *args, **kwargs):
        # Validate serialized data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Create new user
        user = serializer.save()

        # Send Registration SMS
        HostSignupNotificationSMS(user).send(lang='EN')
        HostSignupNotificationSMS(user).send(lang='AM')

        # Generate JWT token
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        # Include user data along with token
        data = jwt_response_payload_handler(token, user, request)
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class HostOwnDetailAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = HostSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        return self.request.user


class HostSignupNotificationEN(BaseSMSView):
    url = 'admin:accounts_customuser_change'
    model = User
    sms_class = HostSignupNotificationSMS
    sms_name = 'HOST signup notification (English)'
    lang = LANG_ENGLISH


class HostSignupNotificationAM(BaseSMSView):
    url = 'admin:accounts_customuser_change'
    model = User
    sms_class = HostSignupNotificationSMS
    sms_name = 'HOST signup notification (Amharic)'
    lang = LANG_AMHARIC
