# let's say users has hundred thousands of objects
users = User.objects.all()

# iterator(chunk_size=1000) will only store 1000 objects in memory/cache at a time to help with the heavy querying/decreasing memory consumption
for user in users.iterator(chunk_size=1000):
    user.full_name = f'{user.first_name} {user.last_name}'
    user.save()
