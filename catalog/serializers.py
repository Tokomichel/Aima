from rest_framework import serializers

from catalog.models import Artist, Album, Track

#Serializers

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio']

    def create(self, validated_data):
        return Artist.objects.create(**validated_data)


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'artist', 'release_date', 'cover_url']

    def create(self, validated_data):
        return Album.objects.create(**validated_data)

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'title', 'album', 'artist', 'duration', 'file_url']

    def create(self, validated_data):
        return Track.objects.create(**validated_data)