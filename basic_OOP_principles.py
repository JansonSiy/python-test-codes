# "class"
# A class is a blueprint for creating objects
class Dog:
    # "class attributes"
    # Class attributes are attributes that have the same value for all class instances
    legs = 4
    eyes = 2

# generate output
print(Dog.legs)


# "inheritance"
# sample #1
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_add_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Address(BaseModel):
    state = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    pin_code = models.IntegerField()

 
# sample #2
class BaseSoftDeletableModel(models.Model):
    is_deleted = models.Boolean(default=False)
    deleted_at = models.DateTimeField(null=True)
    deleted_by = models.ForeignKey(User, null=True)
    
    class Meta:
        abstract = True
        
    def soft_delete(self, user_id=None):
        self.is_deleted = True
        self.deleted_by = user_id
        self.deleted_at = timezone.now()
        self.save()


class Address(BaseModel, BaseSoftDeletableModel):
    state = models.CharField(max=10)
    country = models.CharField(max=10)
    pin_code = models.IntegerField()

# output
# In [1]: address = Address.objects.create(state='KR', country='IN', pin_code=111111)

# In [2]: address.__dict__
# Out[2]: 
# {
#     '_state': <django.db.models.base.ModelState at 0x113d15fa0>,
#      'id': 1,
#      'created_at': datetime.datetime(2021, 7, 2, 6, 53, 57, 140334, tzinfo=<UTC>),
#      'updated_at': datetime.datetime(2021, 7, 2, 6, 53, 57, 140368, tzinfo=<UTC>),
#      'is_deleted': False,
#      'deleted_by_id': None,
#      'deleted_at': None,
#      'state': 'KR',
#      'country': 'IN',
#      'pin_code': 111111
#  }

# In [3]: address.soft_delete()

# In [4]: address.__dict__
# Out[4]: 
# {
#     '_state': <django.db.models.base.ModelState at 0x113d15fa0>,
#      'id': 1,
#      'created_at': datetime.datetime(2021, 7, 2, 6, 53, 57, 140334, tzinfo=<UTC>),
#      'updated_at': datetime.datetime(2021, 7, 2, 6, 54, 39, 496424, tzinfo=<UTC>),
#      'is_deleted': True,
#      'deleted_by_id': None,
#      'deleted_at': datetime.datetime(2021, 7, 2, 6, 54, 39, 495744, tzinfo=<UTC>),
#      'state': 'KR',
#      'country': 'IN',
#      'pin_code': 111111
#  }


# "multi-table inheritance"
class BaseSoftDeletableModel(models.Model):
    is_deleted = models.Boolean(default=False)
    deleted_at = models.DateTimeField(null=True)
    deleted_by = models.ForeignKey(User, null=True)
    
    class Meta:
        abstract = True
        
    def soft_delete(self, user_id=None):
        self.is_deleted = True
        self.deleted_by = user_id
        self.deleted_at = timezone.now()
        self.save()


class Address(BaseModel, BaseSoftDeletableModel):
    state = models.CharField(max=10)
    country = models.CharField(max=10)
    pin_code = models.IntegerField()
    

class Place(Address):
    name = models.CharField(max=10)

# output
# In [1]: place = Place.objects.create(name='home', state='KR', country='IN', pin_code=13123)

# In [2]: place.__dict__
# Out[2]: 
# {
#     '_state': <django.db.models.base.ModelState at 0x10f8ce1f0>,
#      'id': 2,
#      'created_at': datetime.datetime(2021, 7, 3, 11, 43, 40, 813214, tzinfo=<UTC>),
#      'updated_at': datetime.datetime(2021, 7, 3, 11, 43, 40, 813256, tzinfo=<UTC>),
#      'is_deleted': False,
#      'deleted_by_id': None,
#      'deleted_at': None,
#      'state': 'KR',
#      'country': 'IN',
#      'pin_code': 13123,
#      'address_ptr_id': 2,
#      'name': 'home'
#  }

# In [3]: Address.objects.count()
# Out[3]: 2


# initialization
class Animal:
    legs = 4
    eyes = 2


class Dog(Animal):
    breed = "Bichon Frise"

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def hello(self):
        return "My name is " + self.name


class Name:
    dog = Dog("Polar")

print(dog.legs)
# 4
print(dog.name)
# Polar
print(dog)
# Polar


# super
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=10)

class Book(Product):
    author = models.CharField(max_length=200)

    def __init__(self, *args, **kwargs):
        # additional procesing before saving
        super().__init__(*args, **kwargs)

# Using super().__init__(*args, **kwargs) in this way allows the Book model to inherit the title and price fields from the Product model, while also adding the author field specific to the Book model.

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    last_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.last_modified = timezone.now()
        self.save()

class Book(Product):
    author = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        # Do additional processing here
        super().save(*args, **kwargs)

# In this revised version of the example code, the save method of the Product model saves the model instance after updating the last_modified field. When the save method of the Book model is called, it uses super().save(*args, **kwargs) to call the save method of the Product model, which saves the model instance with the updated last_modified field.