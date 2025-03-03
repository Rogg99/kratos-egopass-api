from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Voyageur, eGoPassGratuit, eGoPassPayant, CarteBancaire, MobileMoney, Paiement
from uuid import uuid4

User = get_user_model()

class BaseAPITestCase(APITestCase):
    def setUp(self):
        # Création d'un utilisateur test
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

class VoyageurTests(BaseAPITestCase):
    def test_create_voyageur(self):
        url = '/api/voyageurs/'
        data = {
            "type_vol": "aller",
            "numero_go_pass": 12345,
            "nom": "Doe",
            "prenom": "John",
            "nationalite": "Française",
            "numero_passeport": "A1234567",
            "compagnie_aerienne": "Air France",
            "numero_vol": "AF123",
            "provenance": "Paris",
            "destination": "Yaoundé",
            "telephone": "+237650000000",
            "adresse_mail": "john.doe@example.com",
            "adresse_residence": "Yaoundé"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class PaiementTests(BaseAPITestCase):
    def setUp(self):
        super().setUp()
        self.go_pass = eGoPassPayant.objects.create()
        self.paiement = Paiement.objects.create(
            id_paiement=uuid4(),
            user=self.user,
            go_pass=self.go_pass,
            statut=True,
            montant=100.0,
            type_paiement="Carte Bancaire",
            reference="PAY12345"
        )
    
    def test_list_paiements(self):
        url = '/api/paiements/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_verify_paiement(self):
        url = f'/api/paiements/{self.paiement.id_paiement}/verify_from_user/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['status'])

class eGoPassGratuitTests(BaseAPITestCase):
    def test_list_egopass_gratuit(self):
        url = '/api/egopassgratuit/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class eGoPassPayantTests(BaseAPITestCase):
    def test_list_egopass_payant(self):
        url = '/api/egopasspayant/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CarteBancaireTests(BaseAPITestCase):
    def test_list_cartes_bancaires(self):
        url = '/api/cartesbancaires/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class MobileMoneyTests(BaseAPITestCase):
    def test_list_mobile_money(self):
        url = '/api/mobilemoney/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)