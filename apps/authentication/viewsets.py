from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView

from .serialisers import RegisterSerializer, ProfileUpdateSerializer,AbonneProfileSerializer,UserSerializer,ProfileSerializer, CustomTokenObtainPairSerializer

User = get_user_model()

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class ProfileViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve the authenticated user's profile",
        responses={200: ProfileSerializer()},
    )
    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = ProfileSerializer(request.user)
        try:
            if serializer.data['role']['name'] == 'ABONNE':
                serializer = AbonneProfileSerializer(request.user)
        except: 
            pass
        return Response(serializer.data)
    


    @swagger_auto_schema(
        operation_description="Update the authenticated user's profile",
        responses={200: ProfileUpdateSerializer()},
    )
    @action(detail=False, methods=['post'])
    def update(self, request):
        profile = request.user  # Get the authenticated user's profile
        
        serializer = ProfileUpdateSerializer(instance=profile, data=request.data, partial=True)  # Allow partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if validation fails

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
