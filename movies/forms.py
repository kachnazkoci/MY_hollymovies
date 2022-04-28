from django import forms

from hollymovies_5.forms import DatePickerDateInput
from movies.models import Movie, Actor, Director



class MovieForm(forms.ModelForm):
    released = forms.DateField(widget=DatePickerDateInput())

    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ['likes', ]


class ActorForm(forms.ModelForm):
    born_at = forms.DateField(widget=DatePickerDateInput())
    movies = forms.ModelMultipleChoiceField(queryset=Movie.objects.all())

    class Meta:
        model = Actor
        fields = '__all__'

    def save(self, commit=True):
        actor = super(ActorForm, self).save(commit=commit)
        actor.movies.add(*self.cleaned_data.get('movies'))
        return actor


class DirectorForm(forms.ModelForm):
    born_at = forms.DateField(widget=DatePickerDateInput())

    class Meta:
        model = Director
        fields = '__all__'

