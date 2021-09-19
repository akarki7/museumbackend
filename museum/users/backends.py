import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from django.contrib.auth.models import User


class JWTAuth(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None

        prefix, token = auth_data.decode("utf-8").split(" ")

        try:
            payload = jwt.decode(token, settings, settings.JWT_SECRET_KEY)
            user = User.objects.get(username=payload["username"])
            return user
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed("Invalid token")
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed("Expired token")
