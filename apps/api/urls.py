from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    VoyageurViewSet,
    eGoPassGratuitViewSet, eGoPassPayantViewSet,
    CarteBancaireViewSet, MobileMoneyViewSet, PaiementViewSet
)

router = DefaultRouter()
router.register(r'voyageurs', VoyageurViewSet)
router.register(r'egopass-gratuit', eGoPassGratuitViewSet)
router.register(r'egopass-payant', eGoPassPayantViewSet)
router.register(r'carte-bancaire', CarteBancaireViewSet)
router.register(r'mobile-money', MobileMoneyViewSet)
router.register(r'paiements', PaiementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
