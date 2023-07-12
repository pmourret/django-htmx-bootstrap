"""
Définit les urls du module films
"""

from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('home/', views.IndexView.as_view(), name="index"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('films/', views.FilmList.as_view(), name="film_list")
]


