from django.urls import path
from .views import artist_list

"""
urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name='artist-list'),
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name='artist-detail'),
    path('albums/', views.AlbumList.as_view(), name='album-list'),
    path('albums/<int:pk>/', views.AlbumDetail.as_view(), name='album-detail'),
    path('tracks/', views.TrackList.as_view(), name='track-list'),
    path('tracks/<int:pk>/', views.TrackDetail.as_view(), name='track-detail'),
]"""

urlpatterns = [
    path('artists/', artist_list, name='artist-list'),
]