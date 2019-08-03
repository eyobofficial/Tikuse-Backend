import factory

from phonenumbers import example_number

from django.contrib.auth import get_user_model

from accounts.models import CustomUser


User = get_user_model()


def generate_phone_number(country_code='ET'):
    """
    Generate valid phone numbers.
    """
    return example_number('ET')


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: f'username{n}')
    full_name = factory.Faker('name')
    phone_number = factory.LazyFunction(generate_phone_number)

    class Meta:
        model = User


class AdminFactory(UserFactory):
    is_staff = True


class GuestFactory(UserFactory):
    role = CustomUser.GUEST


class HostFactory(UserFactory):
    role = CustomUser.HOST
