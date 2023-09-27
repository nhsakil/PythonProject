class PartyAnimal:
    x=0

    def party(self):
        self.x = self.x +1
        print("So far", self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()

print("Type", type(an))
print("Dir", dir(an))

x = 0
for value in range(5):
    x = value+x
print(x)