from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from topshiriq.models import Topshiriq
from uuid import UUID
from rest_framework_simplejwt.tokens import RefreshToken

class TopshiriqAPITestCase(APITestCase):

    def setUp(self):
       
        # Test uchun user UUID larini yaratamiz
        self.user_uuids = [
            "10832be0-4cf8-4fcb-89da-547afffac19b",
            "513c30d3-0c3e-4709-9f55-950a434726ca",
            "7960d47b-347e-4b59-871d-fdd2af8c1715",
            "dd933ec5-78e4-4bf0-9a9c-9251e8f7b20c"
        ]

        # Test uchun JSON ma’lumot
        self.valid_payload = {
            "users": self.user_uuids,
            "topshiriq_turi": "majburiy",
            "urinishlar_soni": "3",
            "boshlanish_vaqti": "2025-01-31",
            "tugash_vaqti": "2025-02-03"
        }

    def test_create_topshiriq_with_jwt(self):
        """JWT token bilan topshiriq yaratish"""
        url = reverse('topshiriq-list')  # DRF ModelViewSet URL
        
        access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM4NTczMDQzLCJpYXQiOjE3MzgzMTM4NDMsImp0aSI6Ijk2YzkyMGI3MjAyMTQ3ZjI5YzYxZTZiMjU3YzFkMWYzIiwidXNlcl9pZCI6IjEwODMyYmUwLTRjZjgtNGZjYi04OWRhLTU0N2FmZmZhYzE5YiJ9.YIK9jIXH1L9o1ti46FZ5h5CiPlq8F8-hdFmigbDdFIw"
        # Tokenni headerga qo‘shamiz
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        print(self.client)

        # API'ga POST so‘rov yuboramiz
        response = self.client.post(url, self.valid_payload, format='json')

        # HTTP 201 Created qaytishini tekshiramiz
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Ma’lumotlar bazaga saqlanganini tekshiramiz
        self.assertTrue(Topshiriq.objects.filter(id=UUID(self.valid_payload["id"])).exists())

        # JSON response ni tekshiramiz
        self.assertEqual(len(response.data["users"]), len(self.valid_payload["users"]))
        self.assertEqual(response.data["topshiriq_turi"], self.valid_payload["topshiriq_turi"])
        self.assertEqual(response.data["urinishlar_soni"], self.valid_payload["urinishlar_soni"])
        self.assertEqual(response.data["boshlanish_vaqti"], self.valid_payload["boshlanish_vaqti"])
        self.assertEqual(response.data["tugash_vaqti"], self.valid_payload["tugash_vaqti"])
