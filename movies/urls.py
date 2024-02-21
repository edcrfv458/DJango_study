from django.urls import path
from .views import movie_list
from .views import actor_list

urlpatterns = [
    path('movies', movie_list),
    path('actors', actor_list), 
]