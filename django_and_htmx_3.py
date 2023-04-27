# Sources:
# https://htmx.org/ 
# Django and HTMX #3 - Listing and Creating Items (with no refresh!) from BugBytes


# MODELS.PY
from django.db import models

class Film(models.Model):
    name = models.CharField(max_length=128, unique=True)
    users = models.ManyToManyField(User, related_name='films')


# TEMPALTE
{% block content %}
    <form>
        {% csrf_token %}
        <input type="text" name='film_name' placeholder="Enter a film"/>
        <button hx-post={% url 'add-film' %} type="submit">Add Film</button>
    </form>

    {% if  films %}
        <ul>
            {% for film in films %}
                <li>{{ film.name }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>You do not have any films on your list</p>
    {% endif %}
{% endblock %}


# URLS.PY
htmx_urlpattern = [
    path('add-film/', views.add_film, name='add-film')
]


# VIEWS.PY
def add_film(request):
    name = request.POST.get('film_name') # from the templates input element
    film = Film.objects.create(name=name)
    request.user.films.add(film)
    films = request.user.films.all()

    context = {
        'films': films,
    }
    return render(request, 'index.html', context)
