class Player():
    def __init__(self,name,healt):
        self.name = name
        self.__healt = healt

    @property
    def health(self):
        print(f'Health is : {self.__healt}')

    @health.setter
    def health(self,value):
        if(value <= 0):
            self.__healt = 0
        elif(value >= 100):
            self.__healt = 100
        else:
            self.__healt = value

pla = Player('batman',100)
pla.health
pla.health = 500
pla.health
pla.health = 50
pla.health