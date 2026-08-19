from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Artist, Album, Track
from .serializers import ArtistSerializer, AlbumSerializer, TrackSerializer

# Create your views here.

# CRUD Artist: mais pour l'intant on va juste faire une lecture et une modification de l'artiste
@api_view(['GET'])
def artist_list(request: Request) -> Response:
    pass