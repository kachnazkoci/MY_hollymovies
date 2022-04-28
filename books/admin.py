from django.contrib import admin
from books.models import Book
from books.models import Author


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'number_of_pages']
    list_filter = ('number_of_pages',)


admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'born_at')
    list_filter = ('born_at',)


admin.site.register(Author, AuthorAdmin)
