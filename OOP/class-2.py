class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def __str__(self):
        return f'{self.color} - {self.age}'

    def __len__(self):
        return self.age

    def __call__(self, *args, **kwds):
        if (args):
            print('Argumets', args)
        return print("Toy is called")

    def __getitem__(self, key):
        return key * 3


action_figure = Toy("red", 24)

# print(action_figure.__str__())
# print(len(action_figure))
# action_figure()
# action_figure(34, 43)

# print(action_figure[3])
# print(action_figure[31])


class SuperList(list):

    def __init__(self, arr):
        super().__init__(arr)

    def __len__(self):
        return 1000


super_list = SuperList([1, 2, 3, 4])

print(super_list[0])
print(len(super_list))
