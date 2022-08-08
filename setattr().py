class Funko:
    name = 'Superman'
    line = 'Justice League'


print(getattr(Funko,'name'))
# Superman
setattr(Funko, 'name', 'Batman')
print(getattr(Funko,'name'))
# Batman

print(getattr(Funko, 'type', None))
# None
setattr(Funko, 'type', 'None Bobble Head')
print(getattr(Funko,'type'))
# None Bobble Head
