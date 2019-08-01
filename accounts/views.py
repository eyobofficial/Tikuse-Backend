from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer


User = get_user_model()


class SignUpAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
