from django.db import models
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Person(models.Model):
        first_name = models.CharField(max_length=32)
        last_name = models.CharField(max_length=32)

        def __str__(self):
            return f'{self.first_name} {self.last_name}'

class Genre(models.Model):
        name = models.CharField(max_length=32)

        def __str__(self):
            return f'{self.name}'

class PersonMovie(models.Model):
        person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person_movies')
        movie = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='person_movies')
        role = models.CharField(max_length=128, null=True, blank=True)

        def __str__(self):
            return f'{self.person} {self.movie} {self.role}'

class Movie(models.Model):
        title = models.CharField(max_length=128)
        director = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='director_movies')
        screenplay = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='screenplay_movies')
        starring = models.ManyToManyField('Person', related_name='acted_in_movies')
        year = models.IntegerField()
        rating = models.FloatField(
            default=1.0,
            validators=[
                MinValueValidator(1.0),
                MaxValueValidator(10.0)
            ])
        genre = models.ManyToManyField('Genre', related_name='movies')

        def __str__(self):
            return f'{self.title}'



