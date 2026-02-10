from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
import base64
import os

class ReportAPITest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

    def _auth_header(self):
        creds = base64.b64encode(b"testuser:testpass123").decode()
        return f"Basic {creds}"

    def test_report_endpoint(self):
        response = self.client.get(
            "/api/report/1/",
            HTTP_AUTHORIZATION=self._auth_header()
        )
        self.assertIn(response.status_code, [200, 404])
