# Private and Public methods and attributes.
# Private attributes use the single underscore to show that it is private (It's an agreed convention).
class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print('Run')


player1 = PlayerCharacter('Laurent', 100)
player1.run()
