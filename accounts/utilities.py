from .serializers import BaseUserSerializer, HostSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    """
    Return serialized user data along with JWT token
    """
    if user.role == 'HOST':
        SerializerClass = HostSerializer
    else:
        SerializerClass = BaseUserSerializer

    data = {'token': token}
    data.update(SerializerClass(user, context={'request': request}).data)
    return data
