fruits = ("mango", "peach", "grapes")
vegtables = ("corn", "carrots", "potato") 

store = zip(fruits, vegtables)
print(tuple(store))
# output
# (('mango', 'corn'), ('peach', 'carrots'), ('grapes', 'potato'))



# Traversing Lists in Parallel
# https://realpython.com/python-zip-function/
# Python’s zip() function allows you to iterate in parallel over two or more iterables.
# Since zip() generates tuples, you can unpack these in the header of a for loop:

first_name = ("Janson", "Mikka", "Polar")
last_name = ("Siy", "Goot", "Bear")

for f, l in zip(first_name, last_name):
    print(f, l)

    # output
    # Janson Siy
    # Mikka Goot
    # Polar Bear