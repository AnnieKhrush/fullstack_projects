from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'date_of_birth', 'place_of_living', 'user_info')

class UserAddDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'