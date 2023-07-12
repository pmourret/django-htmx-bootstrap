from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, ListView

from films.forms import RegisterForm
from films.models import Film


# Create your views here.


class IndexView(TemplateView):
    template_name = 'pages/home.html'


class Login(LoginView):
    template_name = 'pages/login.html'


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'pages/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FilmList(ListView):
    template_name = 'pages/film-list.html'
    model = Film
    context_object_name = 'films'

    def get_queryset(self):
        user = self.request.user
        return user.films.all()
