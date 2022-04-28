from django.contrib import admin

class HomeAdmin(admin.ModelAdmin):
    list_display = ('books', 'movies', 'contact', 'language')
    list_filter = ('language', )
