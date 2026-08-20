from django.contrib.messages import api
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Artist, Album, Track
from .serializers import ArtistSerializer, AlbumSerializer, TrackSerializer

# Create your views here.

# CRUD Artist: mais pour l'intant on va juste faire une lecture et une modification de l'artiste

#recuperer la liste des artistes
@api_view(['GET'])
def artist_list(request: Request) -> Response:
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

#Recuperer un seul artiste
@api_view(['GET'])
def get_artist(request: Request, pk: int) -> Response:
    try:
        artist = Artist.objects.get(pk=pk)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ArtistSerializer(artist)
    return Response(serializer.data)

#Album
#liste des albums
@api_view(['GET'])
def album_list(request: Request) -> Response:
    albums = Album.objects.all()
    serializer = AlbumSerializer(albums, many=True)
    return Response(serializer.data)


#Recuperer un seul album
@api_view(['GET'])
def get_album(request: Request, pk: int) -> Response:
    try:
        album = Album.objects.get(pk=pk)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AlbumSerializer(album)
    return Response(serializer.data)

#Track
#Recuperer la liste de chanson par auteur
@api_view(['GET'])
def track_list_by_artist(request: Request, artist_id: int) -> Response:
    try:
        artist = Artist.objects.get(pk=artist_id)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    tracks = Track.objects.filter(artist=artist)
    serializer = TrackSerializer(tracks, many=True)
    return Response(serializer.data)

#Recuperer la liste de chanson par album
@api_view(['GET'])
def track_list_by_album(request: Request, album_id: int) -> Response:
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    tracks = Track.objects.filter(album=album)
    serializer = TrackSerializer(tracks, many=True)
    return Response(serializer.data)
