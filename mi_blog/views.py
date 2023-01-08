from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from mi_blog.models import Post, Avatar, Mensaje
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from mi_blog.forms import UsuarioForm
from django.contrib.auth.admin import User
from django.views import View


def index(request):
    posts = Post.objects.order_by("-publicado_el")[0:5]
    post_header = Post.objects.last()
    print(posts)
    return render(request, "mi_blog/index.html", {"posts": posts})


class PostDetalle(DetailView):
    model = Post

class PostListar(ListView):
    model = Post

class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("mi_blog_listar")
    fields = '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("mi_blog_listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("mi_blog_listar")
    fields = "__all__"

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("mi_blog_listar")

class UserLogin(LoginView):
    next_page = reverse_lazy('mi_blog_listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('mi_blog_listar')

class AvatarActualizar(UpdateView):
    model = Avatar 
    fields = ['imagen']
    success_url = reverse_lazy('mi_blog_listar')

class UserActualizar(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('mi_blog_listar')

class MensajeDetalle(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje

class MensajeCrear(SuccessMessageMixin, CreateView):
    model = Mensaje
    success_url = reverse_lazy("mi_blog_mensajes_crear")
    fields = ['nombre', 'email', 'texto']
    success_message = "Mensaje de contacto enviado!!"

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("mi_blog_mensajes_listar")