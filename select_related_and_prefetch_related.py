# sample model
from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=500, null=False)
    city = models.CharField(max_length=50, null=False)
    postcode = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False, unique=True)

class Product(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    price = models.IntegerField(null=False)

class Order(models.Model):
    order_date = models.DateField(null=False)
    shipped_date = models.DateField(null=True)
    delivered_date = models.DateField(null=True)
    coupon_code = models.CharField(max_length=50, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    products = models.ManyToManyField(Product, through='LineItem')

class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=False)

# sample views
from django.shortcuts import render
from .models import Order

def index(request):
    # this is inefficient, it takes too many querys, query from the order model & query from the customer model
    orders = Order.objects.all()

    for order in orders:
        customer_per_order = order.customer

    # context = {'customer_per_order': customer_per_order}

    # return render(request, 'index.html', context)



    # using select_related
    # prerequisite is foreign key relationship, then call the field
    orders = Order.objects.select_related('customer').all()

    for order in orders:
        customer_per_order = order.customer
   
    # context = {'customer_per_order': customer_per_order}

    # return render(request, 'index.html', context)



    # using prefetch_related
    # works with many to many fields than just foreign keys - basically including more than 2 tables
    # the example below only used 2 queries
    orders = Order.objects.prefetch_related('products').all()

    for order in orders:
        for product in order.products.all():
            product_per_order = product

    context = {'product_per_order': product_per_order}

    return render(request, 'index.html', context)