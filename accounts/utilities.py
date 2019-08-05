from .serializers import UserSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    """
    Return serialized user data along with JWT token
    """
    data = {'token': token}
    data.update(UserSerializer(user, context={'request': request}).data)
    return data
