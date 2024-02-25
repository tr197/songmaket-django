from uuid import uuid4
from django.db import models

class Banner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    image = models.ImageField(null=False, blank=False, upload_to="assets/banners/")
    title = models.CharField(null=False, blank=False, max_length=255)