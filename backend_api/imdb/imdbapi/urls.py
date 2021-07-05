
from django.urls import path,include
from .views import *
from imdbapi import views

urlpatterns=[    
    path('movies',Movies.as_view(),name='all-movies'),
    path('movies/create',MovieCreate.as_view(), name='Moviecreate'),
    path('movies/addgenre',MovieAddgenre.as_view(), name='MovieAddgenre'),
    path('movies/<str:pk>', MovieDetail.as_view(), name='MovieDetail'),
    path('movies/delete/<str:pk>', MovieDelete.as_view(), name='MovieDelete'),
    path('movies/update/<str:pk>', MovieUpdate.as_view(), name='MovieUpdate'),
    path('movies/rating', views.Rating, name='Rating'),
    path('movies/search/<movie_name>/', views.Moviesearch, name='Moviesearch')
]