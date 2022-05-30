from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name = 'home'),
    path('search/', views.search_image, name='search_image'),
    path('location/(<image_location>\d+)', views.location_filter, name='location_filter'),
    path('image/(<category_name>\w+)/(<image_id>\d+)',views.single,name = 'single')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)