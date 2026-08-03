class User:

    def __init__(self, name="", age=0, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self._age = age


class Archer(User):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def expose_data(self):
        print(self._age)
        print(self._User__name)


class Wizard(User):
    def __init__(self, power="", **kwargs):
        super().__init__(**kwargs)
        self.power = power

    def print_wizard(self):
        print(f"Wizard name - {self._User__name}")
        print(f"Wizard age - {self._age}")
        print(f"Wizard power - {self.power}")


class SuperWorrior(Archer, Wizard):
    def __init__(self, name, age, power):
        super().__init__(name=name, age=age, power=power)


sup = SuperWorrior("Ansh", 22, "Fire")

sup.print_wizard()
