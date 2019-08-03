from django.urls import path

from .views import SignUpAPIView


app_name = 'v1-accounts'


urlpatterns = [
    path('signup/', SignUpAPIView.as_view(), name='signup')
]
