from django.shortcuts import render
from django.http  import HttpResponse
from .models import Galleryimage

# Create your views here.
def home(request):
    images = Galleryimage.objects
    return render(request, 'home.html', {"images":images})
    