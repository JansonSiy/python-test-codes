# python manage.py shell
# exit()

# sample import in shell
from blog.models import *
# all
from blog.models import Post
# specific model

# displaying all objects from a model
Post.objects.all()

# creating an objects in a model
Post.objects.create(author=me, title='About Earth', body='The earth is round.')

# before we can access me we must import User model first
from django.contrib.auth.models import User

# then, create a variable and use get to target what you need
me = User.objects.get(username='Jan')
myPost = Post.objects.get(title='About Earth')

# filtering objects in a model
Post.objects.filter(author=me)

# or we could use __contains in filtering
Post.objects.filter(title__contains='earth')

# you can also order the list of objects by using order_by
Post.objects.order_by('created_date')

# we can also reverse the ordering by adding - at the beginning
Post.objects.order_by('-created_date')