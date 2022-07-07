# example #1
try:
    number = int('1')
    print(number, 'is now an integer')
except:
    print('your number is not convertable to an integer')

# 1 is now an integer


# example #2
try:
    number = int('abc')
    print(number, 'is now an integer')
except:
    print(number ,'is not convertable to an integer')

# 1 is not convertable to an integer


# example #3
try:
    number = int('abc')
    print(number, 'is now an integer')
except ValueError as e:
    print(e)

# invalid literal for int() with base 10: 'abc'