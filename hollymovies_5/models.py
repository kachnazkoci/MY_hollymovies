from django.db import models
from django.shortcuts import resolve_url


class Home(models.Model):
    LANGUAGE_ENG = 'eng'
    LANGUAGE_CZ = 'cz'

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENG, 'english'),
        (LANGUAGE_CZ, 'czech'),
    )
    def get_absolute_url(self):
        return resolve_url('hollymovies_5',)

class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    subject = models.TextField()
    phone_number = models.IntegerField()
    contact_at = models.DateField()


class BasePersonModel(models.Model):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'

    GENDER_CHOICES = (
        (GENDER_MALE, 'male'),
        (GENDER_FEMALE, 'female')
    )

    name = models.CharField(max_length=256)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
    born_at = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


