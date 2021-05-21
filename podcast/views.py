
# Python
import os


# Rest Framework
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status

# Models

from .models import Podcast
from authentication.models import User

# Utils
from .utils import *

# Serializers

from .serializers import PodcastSerializer

# Services

from .services.upload_podcast import Upload



'''
    POST /upload/
    This endpoint allows user to upload podcast to server
'''

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser])
def upload_podcast(request):
    audio_file = request.FILES['audio']
    image_file = request.FILES['image']
    audio_extension = os.path.splitext(str(audio_file))[1]
    image_extension = os.path.splitext(str(image_file))[1]
    if(audio_extension in ACCEPTED_AUDIO_EXTENSIONS or image_extension in ACCEPTED_IMAGE_EXTENSIONS ):
        
    
        name = request.data['name']
        description = request.data['description']

        user = User.objects.get(username=request.user)

        response = Upload.upload(audio_file,user)

        podcast = Podcast(
            name = name,
            audio_url = response['secure_url'],
            description = description,
        )
        podcast.save()
        podcast.owner.add(user)
        serializer = PodcastSerializer(podcast) 
        

        return Response(data={"upload": True, "response": serializer.data})

    else:
        return Response(data={'upload': False, 'response': 'File extension not valid'}, status=status.HTTP_400_BAD_REQUEST)


'''
    GET / podcasts
    This endpoint allow client to fetch all podcasts 
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def podcasts(request):
    qs = Podcast.objects.all()
    serializer = PodcastSerializer(qs, many=True)
    return Response(serializer.data)


'''
    GET /podcast-by-user/<str:userr>/
    This endpoint allow client to filter by username to get podcasts
'''

def get_podcasts_by_user(request, user):
        try:
            user_instance =  User.objects.get(username=user)
            queryset = Podcast.objects.filter(owner=user_instance)
            serializer = PodcastSerializer(queryset, many=True)
            return Response(data={'response': serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response(data={'response': 'Failed to get podcast. Try again'}, status=status.HTTP_404_NOT_FOUND)

'''
    DELETE /delete-podcast/<str:podcast_name> 
    This endpoint allow client to delete an specific podcast 
'''

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_audio(request, podcast_name):
    user = str(request.user)
    response = Upload.delete(podcast_name, user)
    return Response(data=response, status=status.HTTP_204_NO_CONTENT)


'''
    POST /like/<str:podcast_name>
    This endpoint allow client to like podcasts
'''

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like(request, podcast_name):
    podcast = Podcast.objects.get(name=podcast_name)
    podcast.like += 1
    podcast.save()
    return Response(data={'response': 'Liked'}, status=status.HTTP_200_OK)

'''
    POST /unlike/<str:podcast_name>/
    This endpoint allow client to unlike podcasts
'''

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike(request, podcast_name):
    podcast = Podcast.objects.get(name=podcast_name)
    if podcast.like == 0:
        return Response(data={'Error': 'Not able to unlike podcast'},status=status.HTTP_400_BAD_REQUEST)
    podcast.like -= 1
    podcast.save()
    return Response(data={'response': 'Unliked'}, status=status.HTTP_200_OK)
