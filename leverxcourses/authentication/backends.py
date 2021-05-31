import logging

import jwt
from django.conf import settings
from rest_framework import authentication, exceptions

from .models import User

logger = logging.getLogger()


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Bearer'

    def authenticate(self, request):
        """
        This method is called with every request
        """
        request.user = None
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        elif len(auth_header) > 2:
            return None
        token = auth_header[0].decode('utf-8')
        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
        except Exception:
            msg = 'Error in token decoder'
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            msg = 'User not found'
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = 'User is not active'
            raise exceptions.AuthenticationFailed(msg)
        print("Token is ok")
        return (user, token)
