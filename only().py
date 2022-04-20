# reference - https://docs.djangoproject.com/en/4.0/ref/models/querysets/#django.db.models.query.QuerySet.only

cuisine_names_codes = Cuisine.objects.only('name', 'code')

for each_cuisine in cuisine_names_codes:
    print(each_cuisine.name, each_cuisine.code)