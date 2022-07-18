class PlayerCharacter:
    def __init__(self, name='Anonymous', age=0):
        self.name = name
        self.age = age

    def speak(self):
        print(f'My name is {self.name} and I am {self.age} years old')


player = PlayerCharacter('Laurent', 100)
player.speak()
