from django.http import HttpResponse
from .models import Genre, Person, Movie
from django.shortcuts import render, get_object_or_404



def populate_data(request):
    genre_action = Genre.objects.create(name='Action')
    genre_comedy = Genre.objects.create(name='Comedy')
    genre_drama = Genre.objects.create(name='Drama')

    director = Person.objects.create(first_name='Christopher', last_name='Nolan')
    screenwriter = Person.objects.create(first_name='Jonathan', last_name='Nolan')
    actor1 = Person.objects.create(first_name='Leonardo', last_name='DiCaprio')
    actor2 = Person.objects.create(first_name='Johnny', last_name='Depp')
    actor3 = Person.objects.create(first_name='John', last_name='Jack')
    actor4 = Person.objects.create(first_name='John', last_name='Lenon')
    actor5 = Person.objects.create(first_name='Eddie', last_name='Smith')
    actor6 = Person.objects.create(first_name='Selena', last_name='Arthur')

    movie = Movie.objects.create(
        title='Pirates of Caribien',
        director=director,
        screenplay= screenwriter,
        year=2010,
        rating=5.5
    )

    movie.genre.add(genre_action, genre_comedy)

    return HttpResponse("Databaze uspěšně naplněna")

def movie_list(request):
    movies = Movie.objects.all().order_by('-year')
    return render(request,'movies.html', {'movies':movies})

def movie_detail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    return render(request, 'movie_details.html', {'movie':movie})

def movie_detail(request, movie_id, movie_detail=None):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movie_details.html', {'movie':movie})


