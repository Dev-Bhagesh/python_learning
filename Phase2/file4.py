import random

class GameCharacter:

    GameName = 'Hero Hunter'
    MaxLevel = 100
    def __init__(self,Name,Role,Gender):
        self.health = 100
        self.CharName = Name
        self.CharRole = Role
        self.CharGender = Gender
        # self.CharDamage = 100
        self.defence = 50
        self.attackPower = random.randint(0,100)


    def CharInfo(self):
        print(self.CharName)
        print(self.CharGender)
        print(self.CharRole)

    def TakeDamage(self,Damage):
        self.health = max(self.health - Damage)
        print(f'{self.CharName} : Got damaged of {Damage} -> remaining HP {self.health}')
        # print(self.CharDamage)

    def Attack(self,target):
        print(f'{self.CharName} Attacked {target.CharName} with AttackPower of -> {self.attackPower}')
        target.TakeDamage(self.attackPower)
        # print(f'{target.CharName} got damaged')

hero = GameCharacter('Batman','Hero','Male')
villen = GameCharacter('Joker','villen','Male')

while(hero.health >= 0 or villen.health >= 0):
    turn = random.randint(1,100)
    if turn % 2 == 0:
        hero.Attack(villen)
    else:
        villen.Attack(hero)

    if hero.health <= 0:
        print(f"****** {villen.CharName} Won The Battle ******")
        break
    elif villen.health <= 0:
        print(f"****** {hero.CharName} Won The Battle ******")
        break

