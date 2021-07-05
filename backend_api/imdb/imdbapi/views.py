
from django.shortcuts import render
from rest_framework import generics, status, renderers,viewsets
from .models import *
from rest_framework.renderers import JSONRenderer
from .serializers import  MovieSerializer,GenreSerializer,RatingSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser
from rest_framework.decorators import api_view,permission_classes,renderer_classes
from rest_framework.response  import Response
from rest_framework.views import APIView
from .models import Movie,MovieGenre


#Class based APIview for movie listing where permission level=ANY
class Movies(APIView):
    permission_classes=[AllowAny]
    def get(self, request, format=None):
        queryset=Movie.objects.all() #getting all records from the database
        serialized = MovieSerializer(queryset,many=True) #serializing records
        return Response(serialized.data)


#Class based APIview for genre add fro a movie where permission level=ADMIN , Only admin user can add this
class MovieAddgenre(APIView):
    permission_classes=[IsAdminUser]
    
    def post(self, request):
        genredata=request.data
        serialized=GenreSerializer(data=genredata)
        # If valid serializer then save data to database else return error response
        if serialized.is_valid():
            movieobject=Movie.objects.get(name=genredata['name'])
            genreobject=MovieGenre.objects.create(name=movieobject,genre=genredata['genre'])
            genreobject.save()
            return Response(serialized.data)
        else:
            return Response(serialized._errors)
#Class based APIview for movie create where permission level=ADMIN , Only admin user can create this
class MovieCreate(APIView):
    permission_classes=[IsAdminUser]
    
    def post(self, request):
        moviedata=request.data
        serialized=MovieSerializer(data=moviedata)
        # If valid serializer then save data to database else return error response
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        else:
            return Response(serialized._errors)

#Class based APIview for movie particular moviee list  where permission level=ANY
class MovieDetail(APIView):
    permission_classes=[AllowAny]
    def get(self, request, pk):
        queryset=Movie.objects.filter(name=pk)
        serialized = MovieSerializer(queryset,many=True)
        return Response(serialized.data)


#Class based APIview for deleting particular movie where permission level=ADMIN , Only admin user can delete this
class MovieDelete(APIView):
    permission_classes=[IsAdminUser]
    def delete(self, request, pk):
        try:
            movieobject=Movie.objects.get(name=pk)
            movieobject.delete()
            return Response({"success":"deleted successfully"},status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({"failure":"Movie not found successfully"},status=status.HTTP_400_BAD_REQUEST)


#Class based APIview for updating particular movie where permission level=ADMIN , Only admin user can delete this
class MovieUpdate(APIView):
    permission_classes=[IsAdminUser]
    def put(self, request, pk):
        try:
            movieobject=Movie.objects.get(name=pk)
            movieobject.name=request.data['name']
            movieobject.popularity=request.data['popularity']
            movieobject.imdbscore=request.data['imdbscore']
            movieobject.director=request.data['director']
            movieobject.writer=request.data['writer']
            movieobject.language=request.data['language']
            movieobject.country=request.data['country']
            movieobject.awards=request.data['awards']
            movieobject.description=request.data['description']
            movieobject.save()
            return Response({"success":"updated successfully"},status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({"failure":"Movie not found successfully"},status=status.HTTP_400_BAD_REQUEST)

#function based api view to list movie according to rating
@api_view(['GET'])
@permission_classes([AllowAny])
def Rating(requests):
    queryset=Movie.objects.all().order_by('-imdbscore')
    serialized = RatingSerializer(queryset,many=True)
    return Response(serialized.data)

#function based api view got searching of movie 
@api_view(['GET'])
@permission_classes([AllowAny])
def Moviesearch(requests,movie_name):
    queryset=Movie.objects.filter(name__icontains=movie_name)
    serialized = MovieSerializer(queryset,many=True)
    return Response(serialized.data)