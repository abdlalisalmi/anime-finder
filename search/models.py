from django.db import models
from django.conf import settings
import os

class UploadImage(models.Model):
    image = models.ImageField(upload_to="search_images")


    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super().delete(*args, **kwargs)