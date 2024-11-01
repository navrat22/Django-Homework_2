from django.urls import path
from .views import populate_data, movie_list, movie_detail

urlpatterns = [
    path('populate-data/', populate_data, name='populate_data'),
    path('movies/', movie_list, name='movie_list'),
    path('movie-details/<int:id>/', movie_detail, name='movie_detail'),


]
