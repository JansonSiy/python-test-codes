class Funko:
    name = 'Superman'
    line = 'Justice League'

    
print(getattr(Funko,'name'))
# Superman
print(getattr(Funko, 'line'))
# Justice League

print(getattr(Funko, 'number', None))
None
