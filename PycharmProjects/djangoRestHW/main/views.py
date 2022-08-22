from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Director,Movie,Review
from main.serializers import MovieSerializer,DirectorSerializer,ReviewSerializer

@api_view(['GET'])
def movie_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies,many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def director_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors,many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def reviews_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews,many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_item_view(request,id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error':f'-Movie:{id}- is not found'},status=404)
    serializer = MovieSerializer(movies)
    return Response(data=serializer.data)

@api_view(['GET'])
def director_item_view(request,id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error':f'-Director:{id}- is not found'},status=404)
    serializer = DirectorSerializer(directors)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_item_view(request,id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error':f'-Review:{id}- is not found'},status=404)
    serializer = ReviewSerializer(reviews)
    return Response(data=serializer.data)