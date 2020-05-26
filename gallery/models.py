from django.db import models
import datetime as dt

# Create your models here.
class ImageCategory(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category
    
    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()

    def update_category(self):
        self.update()

class Location(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()

    def update_location(self):
        self.update()

    @classmethod
    def get_location(cls):
        location = cls.objects.all()
        return location

class Galleryimage(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=80)
    summary = models.CharField(max_length=160)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    def update_image(self):
        self.update()

    @classmethod
    def search_by_category(cls, search_category):
        picture_category = cls.objects.filter(category__name__icontains=search_category)
        return picture_category

    @classmethod
    def get_pictures(cls):
        pictures = cls.objects.all()
        return pictures

    @classmethod
    def get_picture_by_id(cls):
        picture_id = cls.objects.get(pk=id)
        return picture_id