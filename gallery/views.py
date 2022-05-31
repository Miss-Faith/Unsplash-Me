from django.shortcuts import render, redirect
from .models import *
from django.http  import HttpResponse, Http404

# Create your views here.

def home(request):
    images = Image.get_images()
    locations = Location.objects.all()
    title = 'Unsplash Me'

    return render(request, 'gallery/home.html', {'title':title, 'images':images[::-1], 'locations':locations})

def single(request,category_name,image_id):
    # images = Image.get_image_by_id(image_id)
    title = 'Image'
    locations = Location.objects.all()
    # category = Category.get_category_id(id = category)
    category = Image.objects.filter(category__name = category_name)
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"gallery/single.html",{'title':title,"image":image, "locations":locations, "category":category})

def search_image(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        return render(request, 'gallery/search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'gallery/search.html', {"message": message})


def location_filter(request, location):
    locations = Location.objects.all()
    location = Location.get_location_id(location)
    images = Image.filter_by_location(location)
    title = f'{location} Photos'
    return render(request, 'gallery/location.html', {'title':title, 'images':images, 'location':location})

