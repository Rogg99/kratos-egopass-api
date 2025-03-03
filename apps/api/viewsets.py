from rest_framework import viewsets
from .models import Voyageur, eGoPassGratuit, eGoPassPayant, CarteBancaire, MobileMoney, Paiement
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.authentication.authentication import CustomAuthentication

from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import action

class VoyageurViewSet(viewsets.ModelViewSet):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Voyageur.objects.all()
    serializer_class = VoyageurSerializer

class eGoPassGratuitViewSet(viewsets.ModelViewSet):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = eGoPassGratuit.objects.all()
    serializer_class = eGoPassGratuitSerializer

class eGoPassPayantViewSet(viewsets.ModelViewSet):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = eGoPassPayant.objects.all()
    serializer_class = eGoPassPayantSerializer

class CarteBancaireViewSet(viewsets.ModelViewSet):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = CarteBancaire.objects.all()
    serializer_class = CarteBancaireSerializer

class MobileMoneyViewSet(viewsets.ModelViewSet):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = MobileMoney.objects.all()
    serializer_class = MobileMoneySerializer

class PaiementViewSet(viewsets.ModelViewSet):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of payments for the authenticated user",
        responses={200: PaiementSerializer(many=True)},
    )
    @action(detail=False, methods=['get'])
    def from_user(self, request):
        payments = Paiement.objects.filter(user=request.user)  # Filter payments by authenticated user
        serializer = PaiementSerializer(payments, many=True)  # Serialize the queryset
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        operation_description="Verify if a payment exists for the authenticated user",
        responses={200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={"status": openapi.Schema(type=openapi.TYPE_BOOLEAN)}
        )}
    )
    @action(detail=True, methods=['get'])
    def verify_from_user(self, request, pk=None):
        payments = Paiement.objects.filter(user=request.user, id=pk).exists()
        return Response({'status': payments}, status=status.HTTP_200_OK)