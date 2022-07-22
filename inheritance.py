class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in!!!')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
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


wizard = Wizard('Merlin', 100, 'merlin@gmail.com')
archer = Archer('Robin', 500)
wizard.attack()
archer.attack()
print(dir(wizard))
