class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, animal):
        self.name = animal
        print(self.name, "Constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

s = PartyAnimal("Sally")
s.party()

j= PartyAnimal("Jim")
j.party()
s.party()