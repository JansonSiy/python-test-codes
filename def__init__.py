class Superhero():
    # __init__ -> it initializes or creates space in memory, to remember details
    # like name, power & team
    def __init__(self, name, power, team):
        self.name = name
        self.power = power
        self.team = team

Superman = Superhero('Clark Kent', 'Strength, Laser Eyes, Freeze Breath', 'Justice League')
Batman = Superhero('Bruce Wayne', 'Intelligence, Martial Arts, Detective Skills', 'Justice League')

# Superman.name
# 'Clark Kent'
# Superman.power
# 'Strenght, Laser Eyes, Freeze Breath'
# Superman.team
# 'Justice League'

# Batman.name
# 'Bruce Wayne'
# Batman.power
# 'Intelligence, Martial Arts, Detective Skills'
# Batman.team
# 'Justice League'
