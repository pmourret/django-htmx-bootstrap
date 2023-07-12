from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = "pages/home.html"


class Login(LoginView):
    template_name = "pages/login.html"

