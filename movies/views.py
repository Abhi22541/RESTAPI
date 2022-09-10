from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Film
from .serlializers import FilmSerializer
from rest_framework import status, serializers


# I had created CURD operation based api using GET POST PUT DELETE METHOD
class MyModel:
    pass





@api_view(['GET'])
def FilmOverview(request):
    movies_urls = {
        'all_films': '/',
        'search by name': '/?name=film_name',
        'search by detail': '/?detail=detail_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/film/pk/delete'
    }

    return Response(movies_urls)


# to add or create movie database using post


@api_view(['POST'])
def add_film(request):
    film = FilmSerializer(data=request.data)

    # validate already existing data
    if Film.objects.filter(**request.data).exists():
        raise serializers.ValidateError('This data is already exists')
    if film.is_valid():
        film.save()
        return Response(film.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# using GET method to retrive data from database.By using this we can retrive data by using name and etc


@api_view(['GET'])
def view_film(request):
    if request.query_params:
        film = Film.objects.filter(**request.query_params.dict())
    else:
        films = Film.objects.all()

    if films:
        data = FilmSerializer(films)
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# Update using post


@api_view(['POST'])
def update_film(request, pk):
    film = Film.objects.get(pk=pk)
    data = FilmSerializer(instance=film, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# DELETE DATA
@api_view(['DELETE'])
def delete_film(request, pk):
    film = get_object_or_404(Film, pk=pk)
    film.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
