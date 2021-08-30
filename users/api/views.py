from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from users.models import Profile
from users.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from blog.models import Post
from blog.api.serializers import PostSerializer

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