# Reference: https://www.geeksforgeeks.org/stringio-module-in-python/#:~:text=The%20StringIO%20module%20is%20an,a%20string%20to%20the%20constructor.

from io import StringIO

# .read()
string = 'This is a string!'
file = StringIO(string)

print(file.read())
# This is a string!





# StringIO.getvalue()
string = 'This string is the value!'
file = StringIO(string)

print(file.getvalue())
# This string is the value!





# FUNCTIONS
string = 'Check me!'
file - StringIO(string)

# StringIO.isatty():This function Return True if the stream is interactive and False if the stream not is interactive
print('interactive:', file.isatty())
interactive: False

# StringIO.readable():This function return True if the file is readable and returns False if file is not readable.
print('readable:', file.readable())
readable: True

# StringIO.writable():This function return True if the file supports writing and returns False if file does not support writing.
print('writable:', file.writable())
writable: True

# StringIO.seekable():This function return True if the file supports random access and returns False if file does not support random access.
print('seekable:', file.seekable())
seekable: True

# StringIO.closed:This function return True if the file is closed and returns False if file is open.
print('closed:', file.closed)
closed: False





# StringIO.seek()
string = 'Seek me!'
file = StringIO(string)

print(file.read())
# Seek me!

# when printing again
print(file.read())
# <empty>

file.seek(0)
0

print(file.read())
# Seek me!





# StringIO.truncate()
string = 'Truncate me!'
file = StringIO(string)

print(file.read())
# Turnicate me!

print(file.read())
# <empty>

file.seek(0)
# 0

file.truncate(3)
# 3

print(file.read())
# Tru





# StringIO.tell()
string = 'Tell them that I am a string!'
file = StringIO(string)

print(file.tell())
# 0

file.seek(3)
# 3

print(file.tell())
# 3





# StringIO.close()
string ='True or False?'
file = StringIO(string)
 
print(file.read())
# True or False?

file.close()
 
print("Is the file closed?", file.closed)
# Is the file closed? True