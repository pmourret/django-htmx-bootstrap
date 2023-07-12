![image_django](https://miro.medium.com/max/1200/1*slHeZngyeUr7ypEz7MNL5w.png)

# Django, Bootstrap CSS & HTMX

## Sommaire
* [Description du dépôt](#description-du-dépôt)
* [Introduction](#introduction)
  * [HX-POST](#lattribut--hx-post)
  * [HX-TRIGGER](#lattribut--hx-trigger)
  * [HX-TARGET](#lattribut--hx-target)
  * [HX-SWAP](#lattribut--hx-swap)
  * [HX-DELETE](#lattribut--hx-delete)
  * [HX-CONFIRM](#lattribut--hx-confirm)
* [Trigger modifiers & transitions CSS](#les-triggers-modifiers-et-les-transitions-css)

## Description du dépôt
## Introduction
### L'attribut : ``hx-post``
L'attribut [``hx-post``](https://htmx.org/attributes/hx-post/) 
permet à un élément d'envoyer une requête POST à l'url spécifiée 
````html
<button hx-post="{% url 'nom_de_l_url' %}">
    Login
</button>
````
### L'attribut : ``hx-trigger``
L'attribut [``hx-trigger``](https://htmx.org/attributes/hx-trigger/) 
spécifie quel type d'événement déclenchera une requête AJAX.
````html
<div hx-get="/clicked" hx-trigger="click">
  Click Me
</div>
````
### L'attribut : ``hx-target``
L'attribut [``hx-target``](https://htmx.org/attributes/hx-target/)
permet de cibler un élément afin de le transformer (différent de l'élément déclencheur).  
Les valeurs de cet attribut sont :  

| VALEUR                | DESCRIPTION                                                  |
|-----------------------|--------------------------------------------------------------|
| CSS Query selector    | Correspond à l'id ou la classe de l'élément                  |
| this                  | L'élément qui a déclenché la requête                         |
| closest CSS selector  | Le parent le plus proche répondant au sélecteur spécifié     |
| find CSS selector     | L'élément fils correspondant au sélecteur spécifié           |
| next CSS selector     | L'élément correspondant au sélecteur spécifié au sein du DOM |
| previous CSS selector | L'élément précédent le 'sender' au sein du DOM               |                                                             |

### L'attribut : ``hx-swap``
L'attribut [``hx-swap``](https://htmx.org/attributes/hx-swap/)
permet de spécifier comment la réponse va être intégré au sein du DOM.

Les valeurs de cet attribut sont :

| VALEUR      | DESCRIPTION                                                  |
|-------------|--------------------------------------------------------------|
| innerHTML   | (Défaut) Remplace l'HTML interne de l'élément cible          |
| outerHTML   | Remplace l'élément cible entier                              |
| beforebegin | Insére la réponse avant l'élément cible                      |
| afterbegin  | Insére la réponse avant le premier enfant de l'élément cible |
| beforeend   | Insére la réponse après le dernier enfant de l'élément cible |
| afterend    | Insére la réponse après l'élément cible                      |
| delete      | Supprime l'élément cible qu'importe la réponse               |
| none        | Ne colle pas le contenu de la réponse                        |

### L'attribut : ``hx-delete``

### L'attribut : ``hx-confirm``



## Les triggers modifiers et les transitions CSS

Les triggers modifiers (modificateur de déclenchement) et les transitions CSS viennent se placer sur 
l'attribut [``hx-trigger``](https://htmx.org/attributes/hx-trigger/).

Ces mots-clefs permettent de déclencer des [transitions CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions) et de modifier leur déclenchement.

````html
<style>
  .smooth{
    transition: all 1s ease-in;
  }
</style>

<div id="color-demo" class="smooth" style="color: red"
     hx-get="/colors" 
     hx-swap="outerhtml"
     hx-trigger="every 1s"
>
  Changement de couleur
</div>
````