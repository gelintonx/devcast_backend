from rest_framework import serializers
from .models import Podcast
from authentication.models import User




class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)



class PodcastSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(many=True,read_only=True )
    class Meta:
        model = Podcast
        fields = '__all__'