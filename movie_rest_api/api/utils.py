from django.middleware.csrf import get_token

from .serializers import UserSerializer


# Returning the user object along with jwt token
def custom_jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={
            'request': request
        }).data,
        'csrf_token': get_token(request)
    }