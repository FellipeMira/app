from django.urls import path
from galeria.views import index, map 
urlpatterns = [
    path('', index, name='index'),
    path('map/', map, name='map')
]