from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken
import jwt
from django.contrib.auth import get_user_model

User = get_user_model()

SECRET_KEY = 'your_jwt_secret_key'  # Replace with your actual secret key
VALID_PERSONAL_KEYS = ['2025@@@sign-kr@t0$']  # Example list of valid keys

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Retrieve headers
        auth_header = request.headers.get('Authorization')
        personal_key = request.headers.get('X-Kratos-Key')

        # Validate presence
        if not auth_header or not personal_key:
            raise AuthenticationFailed('Authorization and Personal Key headers required.')

        # Validate personal key
        if personal_key not in VALID_PERSONAL_KEYS:
            raise AuthenticationFailed('Invalid Personal Key.')

        try:
            token_type, token = auth_header.split()
            if token_type.lower() != 'bearer':
                raise AuthenticationFailed("Invalid token type. Expected 'Bearer'.")

            access_token = AccessToken(token)  # Validate the token
            user = User.objects.get(id=access_token['user_id'])  # Get user from payload

            # return user  # Return the authenticated user

        except User.DoesNotExist:
            raise AuthenticationFailed("User not found.")
        except Exception as e:
            raise AuthenticationFailed("Invalid or expired token. "+str(e))

        return (user, None)
