from django import forms

from books.models import Book, Author
from hollymovies_5.forms import DatePickerDateInput



class BookForm(forms.ModelForm):
    released = forms.DateField(widget=DatePickerDateInput())

    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['likes', ]

class AuthorForm(forms.ModelForm):
    born_at = forms.DateField(widget=DatePickerDateInput())
    books = forms.ModelMultipleChoiceField(queryset=Book.objects.all())

    class Meta:
        model = Author
        fields = '__all__'

    def save(self, commit=True):
        author = super(AuthorForm, self).save(commit=commit)
        author.books.add(*self.cleaned_data.get('books'))
        return author
