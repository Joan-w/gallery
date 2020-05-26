from django.db import models

# Create your models here.
class Galleryimage(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=80)
    summary = models.CharField(max_length=160)

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def update_image(self):
        self.update_image()

    @classmethod
    def search_by_title(cls,search_term):
        result = cls.objects.filter(title_icontains=search_term)
        return result

class Category(models.Model):
    cat_name = models.CharField(max_length =30)

    

class Location(models.Model):
    name = models.CharField(max_length =20)
    date_saved = models.DateTimeField(auto_now_add=True)

    @classmethod
    def today_date(cls):
        today = dt.date.today()
        save_date = cls.objects.filter(date_saved__date = today)
        return save_date