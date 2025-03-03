from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTests(APITestCase):
    def test_user_registration(self):
        url = reverse('register-list')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'strongpassword',
            'bio': 'I am a test user.'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_jwt_login(self):
        user = User.objects.create_user(username='loginuser', password='strongpassword')
        url = reverse('token_obtain_pair')
        data = {'username': 'loginuser', 'password': 'strongpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_profile_access_with_jwt(self):
        user = User.objects.create_user(username='profileuser', password='strongpassword')
        url = reverse('token_obtain_pair')
        data = {'username': 'profileuser', 'password': 'strongpassword'}
        response = self.client.post(url, data, format='json')
        token = response.data['access']

        profile_url = reverse('profile')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        profile_response = self.client.get(profile_url)
        self.assertEqual(profile_response.status_code, status.HTTP_200_OK)
        self.assertEqual(profile_response.data['username'], 'profileuser')
