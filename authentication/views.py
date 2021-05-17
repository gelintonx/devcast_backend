
# Django
from django.shortcuts import render
from django.contrib.auth.hashers import check_password

# Models
from .models import User

#Serializers
from authentication.serializers import RegisterSerializer

# Rest Framework
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        register_serializer = RegisterSerializer(data=request.data)
        if register_serializer.is_valid():
            register_serializer.save()
            user = User.objects.get(username=request.data['username'])
            token = Token.objects.create(user=user)

            return Response({"success": True, "token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response(data=register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):

    if request.method == 'POST':

        username = request.data['username']
        password = request.data['password']

        users = User.objects.get(username=username)

        if users:
            match_password = check_password(password, users.password)

            if match_password == True:

                user = User.objects.get(username=username)
                token, created = Token.objects.get_or_create(user=user)

                return Response({"Authenticated": True, "token": token.key})
            else:
                return Response({"Authenticated": False})
