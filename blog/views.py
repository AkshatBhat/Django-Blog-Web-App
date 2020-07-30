from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

'''def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',context)'''

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html is the naming convention, here we modified it !
    context_object_name = 'posts'
    ordering = ['-date_posted'] # - sign indicates reverse
    paginate_by = 5 # /?page=x after url of home page will lead you to that paginated page

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' 
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username')) 
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    # For this class based view, we followed the naming convention for corresponding template
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    success_url = '/' # after creating a post successfully, redirect to home page

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']
    success_url = '/' # after creating a post successfully, redirect to home page

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self): # To prevent logged in user from updating some other user's post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self): # To prevent logged in user from updating some other user's post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', dict(title="About"))

def announcements(request):
    return render(request, 'blog/announcements.html', dict(title="Announcements"))