# Sources:
# https://htmx.org/ 
# Django and HTMX #1 - Introduction to HTMX and Dynamic AJAX Requests from BugBytes

# Important to understand
# What is AJAX? https://www.w3schools.com/whatis/whatis_ajax.asp 
# What is JSON? https://www.w3schools.com/whatis/whatis_json.asp 


# TEMPLATE
# hx-post: sending a post request
# hx-trigger="keyup": will trigger the action every time user will type any character in the form
# hx-target: replace the element with whatever is return from the backend
# hx-swap: swap the entire element of the hx-target
<head>
    <script src="https://unpkg.com/htmx.org@1.6.0"></script>
</head>
<body>
    {% hx-post="/check_username/" hx-trigger="keyup" hx-target="#username-error" hx-swap="outerhtml" %}
    <div id="username-error"></div>
</body>


# URLS.PY
urlpatterns = [
    ...
]

htmx_urlpatterns = [
    path('check_username/', views.check_username, name='check_username')
]

urlpatterns += htmx_urlpatterns


# FORMS.PY
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


# VIEWS.PY
from django.contrib.auth import get_user_model
from django.http import HttpResponse

def check_username(request):
    # get the 'username' from the form 
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exist():
        return HttpResponse("<div style='color: red;'>This username already exist</div>")
    else:
        return HttpResponse("<div style='color: green;'>This username is available</div>")
