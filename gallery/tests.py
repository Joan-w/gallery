from django.test import TestCase
from .models import Galleryimage, Location, ImageCategory

# Create your tests here.
class ImageTestCase(TestCase):
    def setUp(self):
        pass

    #New picture
    self.new_imagee = title='Image title', summary = 'Image summary')
    self.new_picture.save()

    #New location
    self.new_location = Location(category='Laikipia')
    self.new_location.save()

    #New category
    self.new_category = ImageCategory(category='food')
    self.new_category.save()

    def tearDown(self):
        Galleryimage.objects.all().delete()
        Location.objects.all().delete()
        ImageCategory.objects.all().delete()

class LocationTestClass(TestCase):
    '''
    A test that checks the location of images
    '''
    def setUp(self):
        pass

class ImageCategoryTestClass(TestCase):
    '''
    A test tthat checks the image categories
    '''
    def setUp(self):
        pass
