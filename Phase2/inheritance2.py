class Character():
    def __init__(self,name):
        self.name = name

    def Attack(self):
        print(f'{self.name} Attacked ⚔')

class Knight(Character):
    def Attack(self):
        print(f'{self.name} is a Knight and Attack Using a ⚔')

class Archer(Character):
    def Attack(self):
        print(f'{self.name} is a Archer and Attack using 🏹')

class Wizord(Character):
    def Attack(self):
        print(f'{self.name} is a 🧙‍♂️ and Attack Using Spells and Magic')

knight = Knight('Maximus')
archar = Archer('Silvi')
wizord = Wizord('Strange')
chars = [knight,archar,wizord]
for chars in chars:
    chars.Attack()
