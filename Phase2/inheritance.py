class Vehical():
    def __init__(self,company,model):
        self.company = company
        self.model = model

class Car(Vehical):
    def __init__(self,company,model,door):
        super().__init__(company,model)
        self.door = door

    def CarReputation(self):
        print(f'{self.company} Cars are very good')

    def Model(self):
        print(f'Model of the Car is {self.model}')

class Bike(Vehical):
    def __init__(self,company,model,gear):
        super().__init__(company,model)
        self.gear = gear

    def BikeGear(self):
        print(f'{self.company} Bike of model {self.model} have {self.gear} gears')

    def Model(self):
        print(f'Model of the bike is {self.model}')

CarObj = Car('BMW','M4',4)
CarObj.CarReputation()
CarObj.Model()
BikeObj = Bike('Wolks Vagan','Dukati',5)
BikeObj.BikeGear()
BikeObj.Model()