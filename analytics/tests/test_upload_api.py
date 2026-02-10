from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
import base64
import os

class UploadAPITest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

    def _auth_header(self):
        creds = base64.b64encode(b"testuser:testpass123").decode()
        return f"Basic {creds}"

    def test_csv_upload_success(self):
        file_path = os.path.join(
            os.path.dirname(__file__),
            "test_data.csv"
        )

        with open(file_path, "rb") as f:
            csv_file = SimpleUploadedFile(
                "test_data.csv",
                f.read(),
                content_type="text/csv"
            )

        response = self.client.post(
            "/api/upload/",
            {"file": csv_file},
            HTTP_AUTHORIZATION=self._auth_header()
        )

        self.assertEqual(response.status_code, 201)
