# Example 1
def myFunc(one, two):
	print(one)
	print(two)

myFunc('argumentOne', 'argumentTwo')

# expected output:
# argumentOne
# argumentTwo



# Example 2 *args
def displayArgs(*args):
	print(args)

displayArgs('argsOne', 'argsTwo','argsThree')

# expected output:
# ('argsOne', 'argsTwo', 'argsThree')



# when using a list
def displayArgs_Two(*args):
	print(args)

myList = ['argsOne', 'argsTwo', 'argsThree']

displayArgs_Two(*myList)

# expected output:
# ('argsOne', 'argsTwo', 'argsThree')



# when using arguments and list
def displayArgs_Three(first, second, *args):
	print(first)
	print(second)
	for arg in args:
		print(arg)

myList_Two = ['one', 'two', 'three']

displayArgs_Three('first_arg', 'second_arg', *myList_Two)

# expected output:
# first_arg
# second_arg
# one
# two
# three



# Example 3 *kwargs:
def kwarg_one(**kwargs):
	print(kwargs)

myKwargsList = {'keyOne':'valueOne', 'keyTwo':'valueTwo', 'keyThree':'valueThree'}

kwarg_one(**myKwargsList)

# expected output:
# {'keyOne': 'valueOne', 'keyTwo': 'valueTwo', 'keyThree': 'valueThree'}



# when using a loop
def kwarg_two(**kwargs):
	for key, value in kwargs.items():
		print(key)
		print(value)

myKwargsList_Two = {'keyOne':'valueOne', 'keyTwo':'valueTwo', 'keyThree':'valueThree'}

kwarg_two(**myKwargsList_Two)

# expected output:
# keyOne
# valueOne
# keyTwo
# valueTwo
# keyThree
# valueThree



# or when putting the key and value pair in the argument
def kwarg_three(**kwargs):
	for key, value in kwargs.items():
		print(key)
		print(value)

kwarg_three(keyOne = 'valueOne', keyTwo = 'valueTwo', keyThree = 'valueThree')

# expected output:
# keyOne
# valueOne
# keyTwo
# valueTwo
# keyThree
# valueThree