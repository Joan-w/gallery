from django.shortcuts import render, get_object_or_404
from django.http  import HttpResponse
from .models import Galleryimage, Category

# Create your views here.
def home(request):
    images = Galleryimage.objects
    return render(request, 'home.html', {"images":images})

def details(request, image_id):
    gallery = get_object_or_404(Galleryimage, pk=image_id)
    return render(request, 'details.html', {"gallery":gallery})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Category.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'details.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'details.html',{"message":message})