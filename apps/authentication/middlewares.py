from django.utils.deprecation import MiddlewareMixin
from .models import ActivityLog
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import AnonymousUser


class ActivityLogMiddleware(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Log the Authorization header
        auth_header = request.headers.get('Authorization')
        # Check if the Authorization header is present
        if auth_header is None:
        
            return None  # No action needed, user is anonymous

        # Extract the token from the header
        try:
            token = auth_header.split()[1]  
            # Use JWTAuthentication to validate the token
            jwt_auth = JWTAuthentication()
            validated_token = jwt_auth.get_validated_token(token)  # Validate the token
            user = jwt_auth.get_user(validated_token)  # Get the user from the validated token
            request.user = user  # Set the user to the request
            
            if request.user.is_authenticated:
                action = f"{request.path}"
                # if request.method != "GET": 
                ActivityLog.objects.create(user=request.user, action=action,method=f"{request.method}")
                
            else:
                pass
        except (IndexError, AuthenticationFailed) as e:
            request.user = AnonymousUser()  # Set user to AnonymousUser if authentication fails

        return None  # Continue processing the request
    

class AllowFromMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Set the X-Frame-Options header to allow framing from a specific origin
        response['X-Frame-Options'] = 'ALLOW-FROM http://localhost:5173'
        return response


class ContentSecurityPolicyMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Content-Security-Policy'] = "frame-ancestors 'self' http://localhost:5173"
        return response