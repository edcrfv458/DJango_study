from django.urls import path
from .views import movie_list, movie_detail
from .views import actor_list

urlpatterns = [
    path('movies', movie_list),
    path('actors', actor_list), 
    path('movies/<int:pk>', movie_detail),
]