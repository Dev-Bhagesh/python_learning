from abc import ABC, abstractmethod

class Character(ABC):

    def first(self):
        print('this is first def of Character class')

    @abstractmethod
    def attack(self):
        print('This is attack def of Character')

class Knight(Character):
    def first(self):
        print('this is Knight first def')

    def attack(self):
        pass
        # print('This is Attack of Knight')

class Archer(Character):
    def first(self):
        print('This is archer first def')

    def attack(self):
        pass
        # print('This is attack of Archer')

# character = Character()
knight = Knight()
archer = Archer()

# character.first()
knight.first()
archer.first()

# character.attack()
knight.attack()
archer.attack()