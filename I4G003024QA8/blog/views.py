from pyexpat import model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView

from I4G003024QA8.blog.models import Post



class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model: Post
    fields = '__all__'
    success_url: reverse_lazy("blog:all")
class PostDetailView(DetailView):
    model = Post
class PostUpdateView(UpdateView):
    model =Post
    fields = '__all__'
    success_url: reverse_lazy("blog:all")
class PostDeleteView(UpdateView):
    model =Post
    fields = '__all__'
    success_url: reverse_lazy("blog:all")


# Create your views here.
