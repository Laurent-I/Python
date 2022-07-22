class Toy:
    def __init__(self, color, age):
        self.age = age
        self.color = color
        self.mydict = {
            'name': 'Yoyo',
            'has_pet': False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __del__(self):
        print('deleted!')

    def __call__(self):
        return ('yess?')

    def __getitem__(self, i):
        return self.mydict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])
