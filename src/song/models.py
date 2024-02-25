import uuid
from django.db import models

class Banner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(null=False, blank=False, upload_to='images/banners/')
    title = models.CharField(null=False, blank=False, max_length=255)

    class Meta:
        db_table = 'banner'