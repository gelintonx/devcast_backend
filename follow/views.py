
# Rest Framework
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status

# Models

from .models import Follow
from authentication.models import User



'''
    GET /follow/<str:username>
    This endpoint allow client to follow another client
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def follow(request, username):
    me = User.objects.get(username=str(request.user))
    user = User.objects.get(username=username)
    follow = Follow(
        following=me,
        follower=user
    )
    follow.save()
    return Response(data={'response': 'Followed'}, status=status.HTTP_200_OK)



'''
    GET /unfollow/<str:username>
    This endpoint allow client to unfollow another client
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def unfollow(request, username):
    me = User.objects.get(username=str(request.user))
    user = User.objects.get(username=username)
    follow = Follow.objects.get(following=me,follower=user)
    follow.delete()

    return Response(data={'response': 'Unfollowed'}, status=status.HTTP_200_OK)


'''
    GET /me/followers/>
    This endpoint allow client to get list of own followers
'''

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_followers(request):
    me = User.objects.get(username=str(request.user))
    follow = Follow.objects.filter(follower=me)
    # TODO: check if we should use for loop in case we get a list of qs

    return Response(data={'response': ''}, status=status.HTTP_200_OK)



