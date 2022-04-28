from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.shortcuts import resolve_url
from hollymovies_5.models import BasePersonModel


class Actor(BasePersonModel):
    def get_absolute_url(self):
        return resolve_url('actor_detail', pk=self.pk)


class Director(BasePersonModel):
    def get_absolute_url(self):
        return resolve_url('director_detail', pk=self.pk)


class Movie(models.Model):
    LANGUAGE_ENG = 'eng'
    LANGUAGE_CZ = 'cz'

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENG, 'english'),
        (LANGUAGE_CZ, 'czech'),
    )

    name = models.CharField(max_length=256)
    description = models.TextField()
    rating = models.IntegerField(validators=[
        MinValueValidator(0), MaxValueValidator(100)
    ])
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=5)
    released = models.DateField()
    actors = models.ManyToManyField('Actor', related_name='movies')
    director = models.ForeignKey(
        'Director',
        on_delete=models.SET_NULL,
        related_name='movies',
        null=True, blank=True,
    )
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} : {self.id}'

    def get_absolute_url(self):
        return resolve_url('movie_detail', pk=self.id)



