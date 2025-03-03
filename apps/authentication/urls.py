from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import RegisterViewSet, ProfileViewSet, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

# Router for registration
router = DefaultRouter()
router.register(r'register', RegisterViewSet, basename='register')

urlpatterns = [
    # Registration endpoint
    path('', include(router.urls)),

    # JWT Authentication endpoints
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Protected profile endpoint
    path('profile/', ProfileViewSet.as_view({'get': 'me'}), name='profile'),
    path('profile/update/', ProfileViewSet.as_view({'post': 'update'}), name='profile_update'),
]
