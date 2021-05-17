from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password



class RegisterSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data.get('username'),
            password=make_password(validated_data.get('password')),
            email=validated_data.get('email')
        )

        return user
