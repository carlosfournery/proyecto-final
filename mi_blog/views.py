from django.shortcuts import render
from django.views.generic import ListView, CreateView
from mi_blog.models import Post
from django.urls import reverse_lazy

def index(request):
    return render(request, "mi_blog/index.html", {})


class PostList(ListView):
    model = Post

class PostCrear(CreateView):
    model = Post
    success_url = reverse_lazy("mi_blog_listar")
    fields = '__all__'