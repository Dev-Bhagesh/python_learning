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
        self.attackPower = 10


    def CharInfo(self):
        print(self.CharName)
        print(self.CharGender)
        print(self.CharRole)

    def TakeDamage(self,Damage):
        self.health = self.health - Damage
        # print(self.CharDamage)

    def Attack(self,target):
        target.TakeDamage(self.attackPower)
        print(f'{target.CharName} got damaged')

hero = GameCharacter('Batman','Hero','Male')
villen = GameCharacter('Joker','villen','Male')
villenHealth = villen.health
heroHealth = hero.health
print(f'Batman health : {heroHealth}')
print(f'Joker Heath : {villenHealth}')

hero.Attack(villen)
villenHealth = villen.health
heroHealth = hero.health
print(f'{villenHealth} remaining health of Joker')
print(f'Batman health : {heroHealth}')