# OOP

class PlayerCharacter:
    # Class Attributes
    membership = True

    def __init__(self, name='Anonymous', age=0):
        if age > 18:
            self.name = name
            self.age = age

    def shout(self):
        print(f'My name is {self.name}')

    def run(self):
        print("run")
        return 'done'

    @classmethod
    def adding_thing(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_thing(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Laurent', 19)
player1.attack = 50
print(PlayerCharacter.adding_thing(2, 7))
