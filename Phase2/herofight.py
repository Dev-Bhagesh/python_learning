import random

class GameCharacter:

    GameName = 'Hero Hunter'
    MaxLevel = 100
    def __init__(self,Name,Role,Gender):
        self.RED = "\033[91m"
        self.BLUE = "\033[94m"
        self.GREEN = "\033[92m"
        self.YELLOW = "\033[93m"
        self.RESET = "\033[0m"
        self.health = 100
        self.CharName = Name
        self.CharRole = Role
        self.CharGender = Gender
        self.defence = 50
        self.normalAttack = 10
        self.spacialAttack = 35
        self.HealingPostion = 20
        self.postionCount = 2

    def CharInfo(self):
        print(self.CharName)
        print(self.CharGender)
        print(self.CharRole)

    def HealHP(self):
        self.health += self.HealingPostion
    
    def TakeDamage(self,Damage):
        self.health = max(0,self.health - Damage)
        print(f'💥 {self.RED}{self.CharName} : Got damaged of {Damage} -> remaining HP {self.health}{self.RESET} \n')
        if self.health <= 40 :
            if self.postionCount > 0:
                self.HealHP()
                self.postionCount = self.postionCount - 1
                print(f'{self.GREEN}🔮 {self.CharName}:  healed himself with healing postion and Current HP :{self.health} and remaining postions are :- {self.postionCount} {self.RESET} \n')
            else:
                print(f'{self.YELLOW}{self.CharName}:No more healing potions remaining , potions count : {self.postionCount} {self.RESET} \n')

    def Attack(self,target):
        attackType = random.randint(0,100)
        if attackType % 2 == 0:
            attackDone = self.normalAttack
        else:
            attackDone = self.spacialAttack

        if(self.CharName == 'Batman'):
            logo = "🦇"
        else :
            logo = "🎭"

        print(f'{logo} ⚔️  {self.BLUE}{self.CharName}\033[0m ' f' \033[94mAttacked {target.CharName} with AttackPower of -> {attackDone} {self.BLUE} \n')
        target.TakeDamage(attackDone)

hero = GameCharacter('Batman','Hero','Male')
villen = GameCharacter('Joker','villen','Male')

while(hero.health > 0 or villen.health > 0):
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

