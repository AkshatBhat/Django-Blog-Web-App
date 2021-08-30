from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication

from blog.models import Post
from blog.api.serializers import PostSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
def api_post_detail_view(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({
            'error': 'Blog post does not exist.'
        }, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

# FUNCTION BASED VIEW TO GET LIST OF POSTS
""" @api_view(['GET'])
def api_post_list_view(request):
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        return Response({
            'error': 'Blog posts not found.'
        }, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data) """

# CLASS BASED VIEW TO GET LIST OF POSTS
class ApiPostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    # Uncomment below part, if you need authentication in class based views
    """ authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,) """

@api_view(['GET'])
def api_user_post_list_view(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({
            'error': 'User not found.'
        }, status=status.HTTP_404_NOT_FOUND)

    try:    
        posts = Post.objects.filter(author=user)
    except Post.DoesNotExist:
        return Response({
            'error': 'Blog posts not found.'
        }, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def api_post_update_view(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({
            'error': 'Blog post does not exist.'
        },status=status.HTTP_404_NOT_FOUND)
    
    user = request.user # If Token Authentication is in place, Django will automatically fetch user via token
    if user != post.author:
        return Response({
            'error': "You are not authorized to edit someone else's post."
        }, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        data = dict()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_post_create_view(request):
    post = Post(author=request.user) # Take the user from the request as user is already authenticated using Token Authentication
    
    if request.method == 'POST':
        serializer = PostSerializer(post, data=request.data)
        data = dict()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_post_delete_view(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({
            'error': 'Blog post does not exist.'
        },status=status.HTTP_404_NOT_FOUND)

    user = request.user # If Token Authentication is in place, Django will automatically fetch user via token
    if user != post.author:
        return Response({
            'error': "You are not authorized to delete someone else's post."
        }, status=status.HTTP_401_UNAUTHORIZED)
    
    if request.method == 'DELETE':
        operation = post.delete()
        data = dict()
        if operation:
            data['success'] = 'Delete Successful.'
        else:
            data['error'] = 'Failed to delete post.'
        return Response(data)
