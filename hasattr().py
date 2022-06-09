class Kia:
	model = "Rio"
	year_model = 2015
	color = "dark blue"

print(hasattr(Kia, 'model'))
# expected output:
# True

print(hasattr(Kia, 'wheels'))
# expected output:
# False