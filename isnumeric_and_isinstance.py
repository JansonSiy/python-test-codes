# isinstance
number = 1
# output: 1

check = isinstance(number, int)
# output: True

string = 'Jan'
check = isinstance(string, int)
# output: False



# int
number = '1'
check = int(number)
# output: 1
# output: False



# isnumeric
never_an_int = 'i_am_not_an_int_123'
always_an_int = '123'

check = never_an_int.isnumeric()
# output: False

check = always_an_int.isnumeric()
# output: True