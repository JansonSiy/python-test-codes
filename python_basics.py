# 1 https://www.learnpython.org/en/Variables_and_Types
# my answer
    mystring = 'hello'
    myfloat = float(10.0)
    myint = 20

# 2 https://www.learnpython.org/en/Lists
# my answer
    second_name = names[1]
    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    strings.append('hello')
    strings.append('world')

# 3 https://www.learnpython.org/en/Basic_Operators
# my answer
    x_list = [x] * 10
    y_list = [y] * 10
    big_list = x_list + y_list

# 4 https://www.learnpython.org/en/String_Formatting
# my answer
    print(format_string, "%s %s. Your current balance is $%f." % (data[0], data[1], data[2]))

# 5 https://www.learnpython.org/en/Basic_String_Operations

# 6 https://www.learnpython.org/en/Conditions
# my answer
    number = 16
    second_number = 0
    first_array = [1, 0, 0]
    second_array = [1, 2]

# 7 https://www.learnpython.org/en/Loops
# my answer
    for number in numbers:
        if number == 237:
            break
        if number % 2 == 0:
            continue
        print(number)

# 8 https://www.learnpython.org/en/Functions
# my answer
    def list_benefits():
        return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

    def build_sentence(benefit):
        return "%s is a benefit of functions!"%(benefit)

# 9 https://www.learnpython.org/en/Classes_and_Objects
# my answer
# define the Vehicle class
class Vehicle:
    def __init__(self, name, kind, color, value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value
        
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.kind, self.color, self.value)
        return desc_str
        
# your code goes here
car1 = Vehicle('Fer', 'car', 'red', 60000.00)
car2 = Vehicle('Jump', 'car', 'blue', 10000.00)

# test code
print(car1.description())
print(car2.description())





# VARIABLES & TYPES

# NUMBERS have 2 types, integer(whole number) and floating point(decimals)
# note: two ways to declare a floating point number
myfloat = 7.0
print(myfloat)

ourfloat = float(7)
print(ourfloat)

# STRINGS can be defined either with a single quote or a double quotes
# note: using double quotes makes it easy to include apostrophes (whereas single quotes would terminate the string)
# error: mystring = 'don't worry about apostrophes'
mystring = "don't worry about apostrophes"
print(mystring)

# note: simple operators can be executed on numbers and strings
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# note: assignments can be done on more than one variable "simultaneously" on the same line
# another note: mixing operators between numbers and strings is not supported
a, b = 'jan', 'jeff'
print("this is a = ", a)
print("this is b = ", b)
print("this is a & b = ", a, b)





# STRING FORMATTING
# note: the "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".

# %s - string (or any object with a string representation, like numbers)
# %d - integers
# %f - floating point numbers
# %.<number of digits>f - floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - integers in hex representation (lowercase/uppercase)

name = "Jan"
number = 5
print("Hello %s!" % name)
print("High %d!" % number)

name = "Jan"
age = 27
print("%s is %d years old." % (name, age))





# CONDITIONS
# note: python uses boolean logic to evaluate conditions
x = 2
print("x in inded 2", x == 2)
print("x is not 3", x == 3)
print("x is less than 3", x < 3)

# BOOLEAN OPERATORS
# note The "and" and "or" boolean operators allow building complex boolean expressions
name = "Jan"
age = 27
if name == "John" and age == 27:
    print("Your name is Jan, and you are also 27 years old.")

if name == "Jan" or name == "John":
    print("Your name is either Jan or John.")

# THE "in" OPERATOR
name = "Jan"
if name in ["Jan", "Jeff"]:
    print("Your name is either Jan or Jeff.")

# another if statement
first_statement = False
second_statement = False

if first_statement is True:
    print('first_statement is true')
elif second_statement is True:
    print('second_statement is true')
else:
    print('both statements are false')

# THE "is" OPERATOR
x = [1,2,3]
y = [1,2,3]

print("the value of x is equals to y:", x == y) 
print("x is not y:", x is y)

# THE "not" OPERATOR
print("convert False into True using not operator", not False)
print((not False) == (False))





# LOOPS
# THE "for" LOOP
primes = [2, 3, 5, 7]

for prime in primes:
    print(prime)

for x in range(5):
    print(x)
# prints 0 1 2 3 4

for x in range(3, 6):
    print(x)
# prints 3 4 5

for x in range(3, 8, 2):
    print(x)
# prints 3 5 7

# "while" LOOP
count = 0
while count < 5:
    print(count)
    count += 1
# prints 0,1,2,3,4

# "break" and "continue" statements
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
# prints 0 1 2 3 4

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
# prints out only odd numbers - 1,3,5,7,9

# "else" clause
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))
# prints 0 1 2 3 4 count value reached 5

for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
# prints 1 2 3 4





# FUNCTIONS
def my_function():
    print("Hello From My Function!")

my_function()

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

my_function_with_args("John Doe", "a great year!")

def sum_two_numbers(a, b):
    return a + b

x = sum_two_numbers(1,2)

print(x)





# CLASSES AND OBJECTS

# sampleOne
class User:
    pass

# we call this an instance or an object
user1 = User()
user2 = User()
# first_name and last_ name are what we call fields, they store data specific to user1
# tradionally in Python, field name are sperated by _ if it's two or more and are lowercased
user1.first_name = "Jan"
user1.last_name = "Siy"
user1.age = 27

user2.first_name = "Jeff"
user2.last_name = "Siy"
user2.age = 28

print(user1.first_name)
print(user1.last_name)
print(user1.age)

print(user2.first_name)
print(user2.last_name)
print(user2.age)

# sampleTwo (init method)
# a function inside a class is called method
# init is "initialization or in other laguages called constructor

class Player:
    def_init_(self, full_name, birthday):
        self.full_name = full_name
        self.birthday = birthday

    def say_hi(self):
        print("Hi, my name is ", self.full_name)

    def say_birthday(self):
        print("My birthday is on ", self.birthday)
    
playerOne = Player("Janson Siy", 105994)

print(playerOne.say_hi())
print(playerOne.say_birthday())