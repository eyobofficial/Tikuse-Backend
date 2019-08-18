from django.urls import path

from rest_framework_jwt.views import ObtainJSONWebToken

from .views import HostSignUpAPIView, HostOwnDetailAPIView


app_name = 'v1-accounts'


urlpatterns = [
    path('login', ObtainJSONWebToken.as_view(), name='login'),
    path('hosts/signup', HostSignUpAPIView.as_view(), name='host-signup'),
    path('hosts/me', HostOwnDetailAPIView.as_view(), name='host-own-detail'),
]
