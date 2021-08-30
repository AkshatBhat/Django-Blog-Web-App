from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username_from_author') # Creates a new field => method which returns username for post

    class Meta:
        model = Post
        fields = ['title', 'content', 'date_posted','username']

    def get_username_from_author(self, post):
        username = post.author.username
        return username
