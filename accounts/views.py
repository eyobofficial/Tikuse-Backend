from django.contrib.auth import get_user_model

from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response

from .models import CustomUser
from .serializers import UserSerializer


User = get_user_model()


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

        # Include token key to response
        token = Token.objects.create(user=user)
        data = serializer.data
        data['key'] = token.key
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
