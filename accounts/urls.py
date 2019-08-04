from django.urls import path

from rest_auth.views import LoginView

from .views import HostSignUpAPIView


app_name = 'v1-accounts'


urlpatterns = [
    path('hosts/signup/', HostSignUpAPIView.as_view(), name='host-signup'),
    path('login/', LoginView.as_view(), name='login')
]
