from django.urls import path
from galeria.views import index, map 
urlpatterns = [
    path('', index),
    path('map/',map)
]