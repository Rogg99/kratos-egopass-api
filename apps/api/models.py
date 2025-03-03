from django.db import models
from uuid import uuid4
from apps.authentication.models import *
from django.core.exceptions import ValidationError                                                                                                                                                                        
from django.conf import settings

# Classe de base pour ajouter des champs communs à tous les modèles
class BaseModel(models.Model):
    archived = models.BooleanField(default=False, help_text="Indique si l'enregistrement est archivé.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date de création de l'enregistrement.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Date de la dernière modification.")

    class Meta:
        abstract = True
        ordering = ["-created_at"]

# Modèle représentant un voyageur
class Voyageur(BaseModel):
    TYPE_VOL_CHOICES = [
        ('aller', 'Aller'),
        ('retour', 'Retour'),
        ('aller_retour', 'Aller-Retour')
    ]
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    type_vol = models.CharField(max_length=20, choices=TYPE_VOL_CHOICES)
    numero_go_pass = models.IntegerField()
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    nationalite = models.CharField(max_length=50)
    numero_passeport = models.CharField(max_length=50)
    compagnie_aerienne = models.CharField(max_length=100)
    numero_vol = models.CharField(max_length=50)
    provenance = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    adresse_mail = models.EmailField(max_length=200)
    adresse_residence = models.CharField(max_length=200)

# Modèle pour les eGoPass gratuits
class eGoPassGratuit(BaseModel):
    id_go_pass = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    montant = models.FloatField(null=True, blank=True)

# Modèle pour les eGoPass payants
class eGoPassPayant(BaseModel):
    id_go_pass = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    
# Modèle pour les paiements par carte bancaire
class CarteBancaire(BaseModel):
    numero_carte = models.CharField(max_length=20,primary_key=True,unique=True)
    date_expiration = models.DateField()
    ccv = models.CharField(max_length=4)
    nom_proprietaire = models.CharField(max_length=100)

# Modèle pour les paiements via Mobile Money
class MobileMoney(BaseModel):
    nom_operateur = models.CharField(max_length=50,primary_key=True,unique=True)
    numero = models.CharField(max_length=20)

# Modèle pour les paiements
class Paiement(BaseModel):
    STATUT_CHOICES = [
        (True, 'Succès'),
        (False, 'Échec')
    ]
    
    id_paiement = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True,)
    go_pass = models.OneToOneField(eGoPassPayant, on_delete=models.CASCADE)
    mobile_infos = models.ForeignKey(MobileMoney, on_delete=models.CASCADE,null=True, blank=True,)
    bank_infos = models.ForeignKey(CarteBancaire, on_delete=models.CASCADE,null=True, blank=True,)
    statut = models.BooleanField(choices=STATUT_CHOICES)
    montant = models.FloatField()
    type_paiement = models.CharField(max_length=50)
    reference = models.CharField(max_length=100)
