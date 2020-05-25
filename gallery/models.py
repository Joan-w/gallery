from django.db import models

# Create your models here.
class Galleryimage(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=80)
    summary = models.CharField(max_length=160)