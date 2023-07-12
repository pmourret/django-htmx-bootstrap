from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render

from films.models import Film


# Create your views here.
def check_username(request):
    """
    Cette vue permet un affichage dynamique grâce à HTMX dans le formulaire d'enregistrement
        Parameters:
            request: Objet request
        Returns:
            HttpResponse: HttpResponse - Modifie une div en fonction du traitement
    """
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse(f"<div id='username-error'"
                            f"class='alert alert-danger'>"
                            f"This username already exists !"
                            f"</div>")
    elif username == "":
        return HttpResponse("")
    else:
        return HttpResponse(f"<div id='username-error'"
                            f"class='alert alert-success'>"
                            f"This username is available !"
                            f"</div>")


def check_password_cohesion(request):
    password_first = request.POST.get("password1")
    password_second = request.POST.get("password2")
    if password_first == password_second:
        return HttpResponse(f"<div class='alert alert-success'>"
                            f"The passwords are similar !"
                            f"</div>")
    elif password_first == "" and password_second == "":
        return HttpResponse('')
    else:
        return HttpResponse(f"<div class='alert alert-danger'>"
                            f"The passwords are not similar !"
                            f"</div>")


def add_film(request):
    # Récupération de l'input utilisateur
    name = request.POST.get('film_name')
    # Création d'une nouvelle entrée en BDD
    film = Film.objects.create(name=name)
    # Ajout du nouveau film à la liste de l'utilisateur connecté
    request.user.films.add(film)

    # Retourne un template avec tous les films de l'utilisateur
    films = request.user.films.all()
    return render(request, 'modules/partial-list-film.html', {"films": films})


def delete_film(request, pk):
    # Suppression du film dans la liste de l'utilisateur
    request.user.films.remove(pk)

    # Retourne le fragment de template
    films = request.user.films.all()
    return render(request, 'modules/partial-list-film.html', {"films": films})





