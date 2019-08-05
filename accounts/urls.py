from django.urls import path

from rest_framework_jwt.views import ObtainJSONWebToken

from .views import HostSignUpAPIView


app_name = 'v1-accounts'


urlpatterns = [
    path('hosts/signup/', HostSignUpAPIView.as_view(), name='host-signup'),
    path('login/', ObtainJSONWebToken.as_view(), name='login')
]
