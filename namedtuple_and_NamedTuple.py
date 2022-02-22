from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])

myColor = Color(55, 155, 255)

print(myColor[0])
# output 55

print(myColor.blue)
# output 255



from typing import NamedTuple

class Person(NamedTuple):
    first_name: str
	last_name: str
    age: int

# equivalent to
# Person = collections.namedtuple('Person', ['name', 'age'])

personOne = Person('Jan', 'Siy', 27)

print(personOne)