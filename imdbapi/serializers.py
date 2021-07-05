from rest_framework import serializers
from .models import  Movie,MovieGenre
from rest_framework import serializers

#rating serializer to show rating corresponding to any movie
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name','imdbscore']

#Genre serailizer
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGenre
        fields = ['name','genre']

#movie serializers
class MovieSerializer(serializers.ModelSerializer):
    #including genre column from genre model as both have one to many relationship
    movie_genre = serializers.SlugRelatedField(many=True,
                                                read_only=True,
                                                slug_field='genre')
    class Meta:
        model = Movie
        fields = ['name','popularity','imdbscore','director','date_added','writer',
        'language','country','awards','description','movie_genre']
    def create(self, validated_data,instance=None):
        movie = Movie(name=self.validated_data['name'],
                popularity=self.validated_data['popularity'],
                imdbscore=self.validated_data['imdbscore'],
                director=self.validated_data['director'],
                writer=self.validated_data['writer'],
                language=self.validated_data['language'],
                country=self.validated_data['country'],
                awards=self.validated_data['awards'],
                description=self.validated_data['description'])
        movie.save()
        return movie
        
