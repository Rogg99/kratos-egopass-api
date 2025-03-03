import uuid,os
from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.conf import settings
from django.utils.translation import gettext as _



def profile_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    name, extension = os.path.splitext(instance.photo.name)
    return "profiles/{0}{1}".format(instance.nom_complet, extension)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False,
                          db_index=True, default=uuid.uuid4)
    last_name = models.CharField(blank=False, null=False, max_length=50)
    first_name = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    otp = models.TextField(default='', blank=False, null=False,)
    numero = models.CharField(max_length=20,default='', blank=False, null=False,)
    
    postnom = models.CharField(max_length=100,default='', blank=False, null=False)
    fonction = models.CharField(max_length=100,default='', blank=False, null=False)
    lieu_travail = models.CharField(max_length=100,default='', blank=False, null=False)

    role = models.ForeignKey(
        'Role', 
        verbose_name="Role", 
        on_delete=models.CASCADE,
        related_name="permissions",
        null=True,
        blank=True
    )

    phone_number = models.CharField(max_length=18)

    REQUIRED_FIELDS = [
        'last_name',
        'email',
    ]

    def save(self, *args, **kwargs):  # Corrige la méthode save()
        if self.is_superuser and not self.role:
            role, _ = Role.objects.get_or_create(
                name='SUPERADMIN',
                defaults={'can_has_all_permissions': True}  # Ajout d'un champ par défaut
            )
            self.role = role
        super().save(*args, **kwargs)  # Correction de l'appel super()

        


class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    connexion_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    platform = models.CharField(max_length=150)
    app_name = models.CharField(max_length=150)
    app_version = models.CharField(max_length=150)
    app_code_name = models.CharField(max_length=150)
    user_agent = models.CharField(max_length = 2500)
    
    
class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    method  = models.CharField(max_length = 150, default='', blank=True)
    
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.timestamp}"


class Role(models.Model):
    name = models.CharField("Nom", unique=True, max_length=255)
    can_has_all_permissions = models.BooleanField("Super utilisateur", default=False)

    can_voir_liste_abonnes = models.BooleanField("Voir la liste des abonnes", default=False)
    can_voir_detail_abonne = models.BooleanField("Voir les détails d'un abonne", default=False)
    can_add_abonne = models.BooleanField("Ajouter un abonne", default=False)
    can_update_abonne = models.BooleanField("Modifier un abonne", default=False)
    can_supprimer_abonne = models.BooleanField("Supprimer un abonne", default=False)
    can_archived_abonne = models.BooleanField("Archiver un abonne", default=False)
    can_reset_abonne = models.BooleanField("Restaurer un abonne", default=False)

    can_voir_liste_voyageurs = models.BooleanField("Voir la liste des voyageurs", default=False)
    can_voir_detail_voyageur = models.BooleanField("Voir les détails d'un voyageur", default=False)
    can_add_voyageur = models.BooleanField("Ajouter un voyageur", default=False)
    can_update_voyageur = models.BooleanField("Modifier un voyageur", default=False)
    can_supprimer_voyageur = models.BooleanField("Supprimer un voyageur", default=False)
    can_archived_voyageur = models.BooleanField("Archiver un voyageur", default=False)
    can_reset_voyageur = models.BooleanField("Restaurer un voyageur", default=False)

    can_voir_liste_paiements = models.BooleanField("Voir la liste des paiements", default=False)
    can_voir_detail_paiement = models.BooleanField("Voir les détails d'un paiement", default=False)
    can_add_paiement = models.BooleanField("Ajouter un paiement", default=False)
    can_update_paiement = models.BooleanField("Modifier un paiement", default=False)
    can_supprimer_paiement = models.BooleanField("Supprimer un paiement", default=False)
    can_archived_paiement = models.BooleanField("Archiver un paiement", default=False)
    can_reset_paiement = models.BooleanField("Restaurer un paiement", default=False)

    can_voir_liste_cartebancaires = models.BooleanField("Voir la liste des cartebancaires", default=False)
    can_voir_detail_cartebancaire = models.BooleanField("Voir les détails d'une cartebancaire", default=False)
    can_add_cartebancaire = models.BooleanField("Ajouter une cartebancaire", default=False)
    can_update_cartebancaire = models.BooleanField("Modifier une cartebancaire", default=False)
    can_supprimer_cartebancaire = models.BooleanField("Supprimer une cartebancaire", default=False)
    can_archived_cartebancaire = models.BooleanField("Archiver un cartebancaire", default=False)
    can_reset_cartebancaire = models.BooleanField("Restaurer un cartebancaire", default=False)

    can_voir_liste_agentrvas = models.BooleanField("Voir la liste des agent rva", default=False)
    can_voir_detail_agentrva = models.BooleanField("Voir les détails d'un agent rva", default=False)
    can_add_agentrva = models.BooleanField("Ajouter un agent rva", default=False)
    can_update_agentrva = models.BooleanField("Modifier un agent rva", default=False)
    can_supprimer_agentrva = models.BooleanField("Supprimer un agent rva", default=False)
    can_archived_agentrva = models.BooleanField("Archiver un agent rva", default=False)
    can_reset_agentrva = models.BooleanField("Restaurer un agent rva", default=False)

    can_voir_liste_administrateurs = models.BooleanField("Voir la liste des administrateurs", default=False)
    can_voir_detail_administrateur = models.BooleanField("Voir les détails d'un administrateur", default=False)
    can_add_administrateur = models.BooleanField("Ajouter un administrateur", default=False)
    can_update_administrateur = models.BooleanField("Modifier un administrateur", default=False)
    can_supprimer_administrateur = models.BooleanField("Supprimer un administrateur", default=False)
    can_archived_administrateur = models.BooleanField("Archiver un administrateur", default=False)
    can_reset_administrateur = models.BooleanField("Restaurer un administrateur", default=False)

    can_voir_liste_mobilemoneys = models.BooleanField("Voir la liste des mobilemoneys", default=False)
    can_voir_detail_mobilemoney = models.BooleanField("Voir les détails d'un operateur mobilemoney", default=False)
    can_add_mobilemoney = models.BooleanField("Ajouter un operateur mobilemoney", default=False)
    can_update_mobilemoney = models.BooleanField("Modifier un operateur mobilemoney", default=False)
    can_supprimer_mobilemoney = models.BooleanField("Supprimer un operateur mobilemoney", default=False)
    can_archived_mobilemoney = models.BooleanField("Archiver un mobilemoney", default=False)
    can_reset_mobilemoney = models.BooleanField("Restaurer un mobilemoney", default=False)

    can_voir_liste_egopasss = models.BooleanField("Voir la liste des egopasss", default=False)
    can_voir_detail_egopass = models.BooleanField("Voir les détails d'une egopass", default=False)
    can_add_egopass = models.BooleanField("Ajouter une egopass", default=False)
    can_update_egopass = models.BooleanField("Modifier une egopass", default=False)
    can_supprimer_egopass = models.BooleanField("Supprimer une egopass", default=False)
    can_archived_egopass = models.BooleanField("Archiver une egopass", default=False)
    can_reset_egopass = models.BooleanField("Restaurer une egopass", default=False)

    date_creation = models.DateTimeField("Date de création", auto_now_add=True)
    date_modification = models.DateTimeField("Date de modification", auto_now=True)

    class Meta:
        ordering = ('-date_creation',)

    def __str__(self):
        return self.name
