import factory

from django.contrib.auth import get_user_model

from accounts.models import CustomUser


User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: f'username{n}')
    full_name = factory.Faker('name')

    class Meta:
        model = User


class AdminFactory(UserFactory):
    is_staff = True


class GuestFactory(UserFactory):
    role = CustomUser.GUEST


class HostFactory(UserFactory):
    role = CustomUser.HOST
