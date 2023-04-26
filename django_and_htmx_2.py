# Sources:
# https://htmx.org/ 
# Django and HTMX #2 - Trigger Modifiers and CSS Transitions from BugBytes


# TRIGGER MODIFIERS
# Mainly to avoid sending to many AJAX request
# Both delay and throttle waits the given amount of time before issuing the request
# hx-trigger="delay:1s": If the event triggers again, the countdown is reset
# hx-trigger="throttle:1s": Unlike delay if a new event occurs before the time limit is hit the event will be discarded, so the request will trigger at the end of the time period
# hx-trigger="changed": Only issue a request if the value of the element has changed

# TEMPLATE
<head>
    <script src="https://unpkg.com/htmx.org@1.6.0"></script>
</head>
<body>
    {% hx-post="/check_username/" hx-trigger="keyup delay:2s changed" hx-target="#username-error" hx-swap="outerhtml" %}
    <div id="username-error"></div>
</body>


# CSS TRANSITIONS
# VIEWS.PY
from django.contrib.auth import get_user_model
from django.http import HttpResponse

def check_username(request):
    # get the 'username' from the form 
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exist():
        return HttpResponse("<div id='username-error' class='error'>This username already exist</div>")
    else:
        return HttpResponse("<div id='username-error' class='success'>This username is available</div>")


# CSS
# transition on all of the changes in the style, ease-in means slowly at first and fast at the end with 2 secs duration
.success {
    color: green;
    transition: all ease-in 2s;
}

.error {
    color: red;
    font-size: 50px;
    transform: rotate(45deg);
    transition: all ease-in 2s;
}
