from django.contrib import admin
from .models import Voyageur, eGoPassGratuit, eGoPassPayant, CarteBancaire, MobileMoney, Paiement

class BaseModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('archived', 'created_at', 'updated_at')

@admin.register(Voyageur)
class VoyageurAdmin(BaseModelAdmin):
    list_display = ('nom', 'prenom', 'type_vol', 'compagnie_aerienne', 'numero_vol', 'provenance', 'destination')
    search_fields = ('nom', 'prenom', 'numero_passeport', 'compagnie_aerienne')
    list_filter = ('type_vol', 'compagnie_aerienne', 'nationalite')

@admin.register(eGoPassGratuit)
class eGoPassGratuitAdmin(BaseModelAdmin):
    list_display = ('id_go_pass', 'montant', 'archived')

@admin.register(eGoPassPayant)
class eGoPassPayantAdmin(BaseModelAdmin):
    list_display = ('id_go_pass', 'archived')

@admin.register(CarteBancaire)
class CarteBancaireAdmin(BaseModelAdmin):
    list_display = ('numero_carte', 'nom_proprietaire', 'date_expiration')
    search_fields = ('numero_carte', 'nom_proprietaire')

@admin.register(MobileMoney)
class MobileMoneyAdmin(BaseModelAdmin):
    list_display = ('nom_operateur', 'numero')
    search_fields = ('nom_operateur', 'numero')

@admin.register(Paiement)
class PaiementAdmin(BaseModelAdmin):
    list_display = ('id_paiement', 'go_pass', 'statut', 'montant', 'type_paiement', 'reference')
    search_fields = ('id_paiement', 'type_paiement', 'reference')
    list_filter = ('statut', 'type_paiement')

