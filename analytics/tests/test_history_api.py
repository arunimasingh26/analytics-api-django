from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
import base64
import os

class HistoryAPITest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

    def _auth_header(self):
        creds = base64.b64encode(b"testuser:testpass123").decode()
        return f"Basic {creds}"
    
    def test_history_with_auth(self):
        response = self.client.get(
            "/api/history/",
            HTTP_AUTHORIZATION=self._auth_header()
        )
        self.assertEqual(response.status_code, 200)
