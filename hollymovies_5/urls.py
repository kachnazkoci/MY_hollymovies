from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from hollymovies_5 import views
from hollymovies_5.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls'), name='movies'),
    path('books/', include('books.urls'), name='books'),
]

urlpatterns += staticfiles_urlpatterns()

