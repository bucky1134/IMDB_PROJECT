from django.contrib import admin

# Register your models here.
from .models import  Movie,MovieGenre
admin.site.register(MovieGenre)
admin.site.register(Movie)