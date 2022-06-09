class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    @property
    def full_name(self):
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name

    
name = Employee('Janson', 'Siy')

name.full_name
'Janson Siy'