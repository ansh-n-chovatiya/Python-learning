class User:

    def __init__(self, config={"name": "", "age": 0}):
        self.__name = config["name"]
        self._age = config["age"]

    def sign_in(self):
        print("Signed In")


class Archer(User):

    def __init__(self, config={"name": "", "age": 0}):
        super().__init__(config)

    def expose_data(self):
        print(self._age)
        print(self._User__name)


class Barbarian(User):
    pass


class Wizard(User):
    def __init__(self, name, age):
        super().__init__({"name": name, "age": age})


wizard1 = Wizard("Ansh", 22)
wizard1.sign_in()
print(wizard1._age)
print(wizard1._User__name)

a1 = Archer({
    "name": "A1",
    "age": 33
})

a1.expose_data()

print(isinstance(a1, Archer))
print(isinstance(a1, User))
print(isinstance(wizard1, Archer))
print(isinstance(wizard1, object))
