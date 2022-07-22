class User:
    def sign_in(self):
        print('Logged in!!!')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')

    def check_arrows(self):
        print(f'checking arrows: arrows left: {self.num_arrows}')

    def run(self):
        print('Ran really fast!')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)


hb1 = HybridBorg('Laurent', 2000, 1333)
print(hb1.check_arrows())
print(hb1.attack())
print(hb1.sign_in())
# wizard = Wizard('Merlin', 100)
# archer = Archer('Robin', 500)
# wizard.attack()
# archer.attack()
# print(dir(wizard))
