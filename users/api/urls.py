from django.urls import path,include
from users.api.views import *
from blog.api.views import *
from rest_framework.authtoken.views import obtain_auth_token

# api/user/
urlpatterns = [
    path('register/', api_registration_view, name='api-register'), 
    path('login/', obtain_auth_token, name='api-login'), 
    path('<str:username>/', api_user_post_list_view, name='api-user-posts'),
]