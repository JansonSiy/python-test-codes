from django.http import HttpResponse
import csv

def exportProducts(request):
    # since your are dealing with a CSV file, your content_type should be text/csv
    response = HttpResponse(content_type='text/csv')
    
    # then you need to create a CSV writer
    writer = csv.writer(response)
    # after which create the header of the CSV file
    writer.writerow(['Name', 'Price', 'Quantity', 'Image URL', 'Description'])
    
    # for this part, looping was a better thing to do
    # what you are doing is getting all the values of the keys declared in the header by using .values_list then, writing a row for each set of product values
    for product in Product.objects.all().values_list('name', 'price', 'quantity', 'image', 'description'):
        writer.writerow(product)

    # for the last part, this tells the browser what to do with the response, in this case treat it as an attachment
    response['Content-Disposition'] = 'attachment; filename="products.csv"'
    
    return response