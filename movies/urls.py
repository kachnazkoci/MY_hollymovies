from django.urls import path

from movies import views
from movies.views import ActorListView, MovieListView, MovieDetailView, \
    ActorDetailView, Jinja2TestingView, DirectorListView, DirectorDetailView, CreateMovieView, \
    CreateActorView, UpdateMovieView, UpdateActorView, DeleteMovieView, DeleteActorView, CreateDirectorView, \
    UpdateDirectorView, DeleteDirectorView
from hollymovies_5.views import ContactView, HomeView

urlpatterns = (
    path('', HomeView.as_view(), name=''),
    path('actors/', ActorListView.as_view(), name='actors'),
    path('movies/', MovieListView.as_view(), name='movies'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('actor/<int:pk>/', ActorDetailView.as_view(), name='actor_detail'),
    path('directors/', DirectorListView.as_view(), name='directors'),
    path('director/<int:pk>/', DirectorDetailView.as_view(), name='director_detail'),
    path('testing/', Jinja2TestingView.as_view(), name='jinja2_testing_view'),
    path('contact/', ContactView.as_view(), name='contact_view'),
    path('movie/create/', CreateMovieView.as_view(), name='create_movie'),
    path('actor/create/', CreateActorView.as_view(), name='create_actor'),
    path('movie/update/<int:pk>/', UpdateMovieView.as_view(), name='update_movie'),
    path('actor/update/<int:pk>/', UpdateActorView.as_view(), name='update_actor'),
    path('movie/delete/<int:pk>/', DeleteMovieView.as_view(), name='delete_movie'),
    path('actor/delete/<int:pk>/', DeleteActorView.as_view(), name='delete_actor'),
    path('director/create/', CreateDirectorView.as_view(), name='create_director'),
    path('director/update/<int:pk>/', UpdateDirectorView.as_view(), name='update_director'),
    path('director/delete/<int:pk>/', DeleteDirectorView.as_view(), name='delete_director'),
    path('search_location/', views.search_location, name='search_location')
)
