from django.db import models

from django.contrib.auth.models import User

# List of choices for genres
Genrechoice = [
    ("Adventure", "Adventure"),
    ("Family", "Family"),
    ("Fantasy", "Fantasy"),
    ("Musical", "Musical"),
    ("Animation", "Animation"),
    ("Romance", "Romance"),
    ("Drama", "Drama"),
    ("Thriller", "Thriller"),
    ("Mystery", "Mystery"),
    ("Horror", "Horror")
      
]

#Created movie model as per reuqired feilds

class Movie (models.Model):
    name = models.CharField(max_length=255, unique=True,primary_key=True)
    popularity = models.CharField(max_length=5, null=True)
    imdbscore = models.CharField(max_length=5, null=True)
    director = models.CharField(max_length=255,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    writer = models.CharField(max_length=255,null=True)
    language = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    awards = models.TextField(null=True)
    description = models.TextField(null=True)
    
    def __str__(self):
        return self.name
#Created genre model seprately as one movie can have multiple genres , so to main this foreign key relations is used
class MovieGenre(models.Model):
    name = models.ForeignKey(Movie, on_delete=models.CASCADE,related_name='movie_genre')
    genre = models.CharField(max_length=255, null=True,choices=Genrechoice)

    def __str__(self):
        return f"{self.name} genre name: {self.genre}"

