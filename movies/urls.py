from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, ),
    path('movielist/', views.movie_list, name='movie_list'),
    path('movie/add/', views.movie_add, name='movie_add'),
    path('movie/<int:pk>/edit/', views.movie_edit, name='movie_edit'),
    path('movie/<int:pk>/delete/', views.movie_delete, name='movie_delete'),
]
