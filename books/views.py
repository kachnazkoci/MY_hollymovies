from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from books.models import Book, Author
from books.forms import BookForm, AuthorForm


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'number_of_books': Book.objects.all().count(),
            'number_of_authors': Author.objects.all().count(),
            'page_name': 'Home'
        }
        return TemplateResponse(request, 'hollymovies_5.html', context=context)


class BookListView(ListView):
    model = Book
    template_name = 'books.html'
    extra_context = {'page_name': 'Books'}


class CreateBookView(CreateView):
    template_name = 'book_create.html'
    form_class = BookForm
    model = Book
    extra_context = {'page_name': 'Creat Book'}


class BookDetailView(DetailView):
    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context.update({'page_name': self.object.title})
        return context

    model = Book
    template_name = 'book_detail.html'
    extra_context = {'page_name': 'Book Detail'}

    def post(self, request, pk, *args, **kwargs):
        book = self.get_object()
        book.likes += 1
        book.save(update_fields=['likes', ])
        return redirect('book_detail', pk=pk)



class UpdateBookView(UpdateView):
    template_name = 'book_update.html'
    form_class = BookForm
    model = Book
    extra_context = {'page_name': 'Book Update'}


class DeleteBookView(DeleteView):
    template_name = 'book_confirm_delete.html'
    model = Book
    success_url = reverse_lazy('books')
    extra_context = {'page_name': 'Delete Book'}


class AuthorListView(ListView):
    model = Author
    template_name = 'authors.html'
    extra_context = {'page_name': 'Authors'}


class CreateAuthorView(CreateView):
    template_name = 'author_create.html'
    form_class = AuthorForm
    model = Author
    extra_context = {'page_name': 'Create Author'}


class AuthorDetailView(DetailView):
    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context.update({'page_name': self.object.name})
        return context

    model = Author
    template_name = 'author_detail.html'
    extra_context = {'page_name': 'Author Detail'}



class UpdateAuthorView(UpdateView):
    template_name = 'author_update.html'
    form_class = AuthorForm
    model = Author
    extra_context = {'page_name': 'Author Update'}


class DeleteAuthorView(DeleteView):
    template_name = 'author_confirm_delete.html'
    model = Author
    success_url = reverse_lazy('authors')
    extra_context = {'page_name': 'Delete Author'}
