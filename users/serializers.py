from rest_framework import serializers

from users.models import User

#Serializers

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # On extrait le mot de passe
        password = validated_data.pop('password')
        
        # On crée l'instance de l'utilisateur avec le reste des données
        user = User(**validated_data)
        
        # On hache le mot de passe de manière sécurisée
        user.set_password(password)
        user.save()
        
        return user
