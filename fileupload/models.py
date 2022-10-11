from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


class FileUploader(models.Model):
    description = models.CharField(max_length=255, blank=True)
    upload_file = models.FileField(upload_to='CSV/',
                                   validators=[FileExtensionValidator(['csv', ])],
                                   )
    uploaded_at = models.DateTimeField(auto_now_add=True)
