from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Role

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        role, _ = Role.objects.get_or_create(
            name='ABONNE',
            defaults={
                "can_voir_detail_abonne": True,
                "can_update_abonne": True,
                "can_archived_abonne": True,
                "can_add_voyageur": True,
                "can_update_voyageur": True,
                "can_supprimer_voyageur": True,
                "can_archived_voyageur": True,
                "can_voir_liste_paiements": True,
                "can_voir_detail_paiement": True,
                "can_add_paiement": True,
                "can_voir_liste_cartebancaires": True,
                "can_voir_detail_cartebancaire": True,
                "can_add_cartebancaire": True,
                "can_update_cartebancaire": True,
                "can_archived_cartebancaire": True,
                "can_voir_liste_egopasss": True,
                "can_voir_detail_egopass": True
                } 
        )
        
        user = User.objects.create_user(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['email'],
            email = validated_data['email'],
            password = validated_data['password'],
            # numero=validated_data['numero'],
            role=role,
        )
        return user


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','numero','postnom','fonction','lieu_travail']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        # fields = '__all__'  # Include all fields of Role
        exclude = ('date_creation', 'date_modification', 'id')

class ProfileSerializer(serializers.ModelSerializer):
    role = RoleSerializer()  # Nesting the RoleSerializer
    class Meta:
        model = User
        fields = ['id', 'first_name','last_name','username', 'email','role','numero','postnom','fonction','lieu_travail']


class AbonneProfileSerializer(serializers.ModelSerializer):
    role = RoleSerializer()  # Nesting the RoleSerializer
    class Meta:
        model = User
        fields = ['id', 'first_name','last_name', 'email','role','numero']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token
