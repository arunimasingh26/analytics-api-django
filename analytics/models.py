from django.db import models

# Create your models here.

class Dataset(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_name = models.CharField(max_length=255)
    summary = models.JSONField()

    def __str__(self):
        return self.file_name
