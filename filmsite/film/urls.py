from django.urls import path
from .views import *

urlpatterns = [
    path('', FilmHome.as_view(), name='home'),
    path('film/<str:film_name>/', ShowFilm.as_view(), name='film'),
    path('search/', search_film, name='search_film'),
    path('category/<str:cat_name>/', ShowFilmCategory.as_view(), name='category'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register')
]
