from rest_framework import serializers
from .models import  Voyageur, eGoPassGratuit, eGoPassPayant, CarteBancaire, MobileMoney, Paiement


class VoyageurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voyageur
        exclude = ('created_at', 'updated_at', 'archived')

class eGoPassGratuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = eGoPassGratuit
        exclude = ('created_at', 'updated_at', 'archived')

class eGoPassPayantSerializer(serializers.ModelSerializer):
    class Meta:
        model = eGoPassPayant
        exclude = ('created_at', 'updated_at', 'archived')

class CarteBancaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarteBancaire
        exclude = ('created_at', 'updated_at', 'archived')

class MobileMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileMoney
        exclude = ('created_at', 'updated_at', 'archived')

class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        exclude = ('created_at', 'updated_at', 'archived')


class VerifyPaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = ['id_paiement', 'user__id']



