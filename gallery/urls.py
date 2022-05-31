from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name = 'home'),
    path('search/', views.search_image, name='search'),
    path('location/<location>', views.image_location, name='location'),
    path('image/<category_name>/<image_id>',views.single,name = 'single')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)