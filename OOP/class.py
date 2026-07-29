class PlayerCharacters:

    membership = False

    def __init__(self, name, config={}):
        self.name = name
        self.membership = config["membership"] if config else False

    def getCharacterInfo(self):
        return {"name": self.name}

    def printSelf(self):
        return self

    @classmethod
    def sum(cls, v1, v2):
        return v1 + v2

    @staticmethod
    def sum_static(v1, v2):
        return v1 + v2


pl1 = PlayerCharacters("Ansh", {"membership": True})
pl2 = PlayerCharacters("Nayan", {"membership": True})
pl3 = PlayerCharacters("Chirag")
pl4 = PlayerCharacters("Samay", {"membership": False})

print(pl1.getCharacterInfo())
print(pl1.membership)
print(pl2.membership)
print(pl3.membership)
print(pl4.membership)

# help(pl1)
print(PlayerCharacters.sum(3, 9))
print(PlayerCharacters.sum_static(3, 9))

print(pl4.printSelf())
