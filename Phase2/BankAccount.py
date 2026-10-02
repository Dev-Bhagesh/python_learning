import uuid
class InvalidAmount(Exception):
    pass

class Bank():
    def __init__(self,name,amount = 500):
        try:
            self.ID = uuid.uuid4()
            self.name = name
            self.amount = amount
            if amount > 0:
                self.__balance = amount
            else:
                raise InvalidAmount('Invalid Amount')
        except InvalidAmount as e:
            print(e)

    def showInfo(self):
        print(self.ID)
        print(self.name)
        print(self.__balance)

bhagesh = Bank('Bhagesh')
bhagesh.showInfo()