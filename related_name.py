# model
class Profile(models.Model)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created = AutoCreatedField()

     def __str__(self):
        return self.name

# views
def exportUsers(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Username', 'First Name', 'Last Name', 'Email', 
                     'Age', 'Gender', 'Address', 'Status', 'Date Created'])

    for user in User.objects.all().select_related('profile'):
        writer.writerow([user.username, user.first_name, user.last_name, user.email, 
                        user.profile.age, user.profile.gender, user.profile.address, user.profile.status, user.profile.created])

    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    return response