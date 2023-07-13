from django.urls import path
from . import views

urlpatterns = [
    path("check_username/", views.check_username, name="check_username"),
    path("check_passwords/", views.check_password_cohesion, name="check_passwords"),
    path("add_film/", views.add_film, name="add_film"),
    path("delete-film/<int:pk>", views.delete_film, name="delete-film"),
    path("search-film/", views.search_film, name="search-film"),
    path("clear-messages/", views.clear_messages, name="clear-messages")
]
