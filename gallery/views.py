from django.shortcuts import render, get_object_or_404
from django.http  import HttpResponse
import datetime as dt
from .models import Galleryimage

# Create your views here.
def home(request):
    images = Galleryimage.objects
    return render(request, 'home.html', {"images":images})

def search_result(request):
    if 'image' in request.GET and request.GET['image']:
        search_category = request.GET.get("image")
        searched_results = Image.search_by_category(search_category)
        message = f"{search_by_category}"

        return render(request, 'search.html', {"message":message, "images":searched_results})
    else:
        message = 'I don\'t think you\'ve searched by category'
        return render(request, 'search.html', {"message":message})