from rest_framework import serializers

from catalog.models import Artist

#Serializers

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio']

    def create(self, validated_data):
        return Artist.objects.create(**validated_data)
