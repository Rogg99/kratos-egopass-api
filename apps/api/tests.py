from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Voyageur, eGoPassGratuit, eGoPassPayant, CarteBancaire, MobileMoney, Paiement
from django.contrib.auth import get_user_model

User = get_user_model()

class VoyageurTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.voyageur_data = {
            'type_vol': 'aller',
            'numero_go_pass': 12345,
            'nom': 'Jane',
            'prenom': 'Doe',
            'nationalite': 'FR',
            'numero_passeport': 'A1234567',
            'compagnie_aerienne': 'Airways',
            'numero_vol': 'AW123',
            'provenance': 'Paris',
            'destination': 'New York',
            'telephone': '555123456',
            'adresse_mail': 'jane.doe@example.com',
            'adresse_residence': '123 Main St'
        }

    def test_create_voyageur(self):
        url = reverse('voyageur-list')
        response = self.client.post(url, self.voyageur_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_voyageurs(self):
        url = reverse('voyageur-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class eGoPassGratuitTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.egopass_data = {
            'montant': 0.0
        }

    def test_create_egopass_gratuit(self):
        url = reverse('egopass-gratuit-list')
        response = self.client.post(url, self.egopass_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_egopass_gratuit(self):
        url = reverse('egopass-gratuit-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class PaiementTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.paiement_data = {
            'montant': 100.0,
            'type_paiement': 'Mobile Money',
            'statut': True,
            'reference': 'PAY12345'
        }

    def test_create_paiement(self):
        url = reverse('paiements-list')
        response = self.client.post(url, self.paiement_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_paiements(self):
        url = reverse('paiements-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
