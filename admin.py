from django.contrib import admin
from .models import Person, Genre, Movie, PersonMovie

admin.site.register(Person)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(PersonMovie)
