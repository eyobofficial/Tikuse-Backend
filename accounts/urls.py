from django.urls import path

from rest_auth.views import LoginView

from .views import SignUpAPIView


app_name = 'v1-accounts'


urlpatterns = [
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login')
]
