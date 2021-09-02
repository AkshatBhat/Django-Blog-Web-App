from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from users.models import Profile
from users.api.serializers import *
from rest_framework.authtoken.models import Token
from blog.models import Post
from blog.api.serializers import PostSerializer
import json

@api_view(['POST'])
def api_registration_view(request):    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = dict()
        if serializer.is_valid():
            user = serializer.save()
            data['success'] = 'Successfully registered a new user.'
            data['username'] = user.username
            data['email'] = user.email
            token = Token.objects.get(user=user).key
            data['token'] = token
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def api_edit_profile_view(request):
    flag = False
    errors = {}
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return Response({
            'error': 'Profile does not exist.'
        },status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        data = dict()
        if 'image' in request.data.keys():
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                data['success'] = 'Successfully updated user profile.'
                data['image'] = serializer.data['image']
                flag = True
            else:
                errors = serializer.errors

        if 'username' or 'email' in request.data.keys():
            user_serializer = UserSerializer(
                request.user,
                data={key:val for key, val in request.data.items() if key != 'image'},
                partial=True
            )
            if user_serializer.is_valid():
                user_serializer.save()
                data['success'] = 'Successfully updated user profile.'
                data['username'] = user_serializer.data['username']
                data['email'] = user_serializer.data['email']
                flag = True
            else:
                flag = False
                errors = user_serializer.errors
        
        if flag:
            return Response(data)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)