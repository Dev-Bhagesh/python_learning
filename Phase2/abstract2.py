from abc import ABC,abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self,amount):
        pass

    @abstractmethod
    def validate(self,amount):
        pass

    def recipt(self,amount):
        recipt = { 'Money' : amount, 'Transfered' : True, 'Method':self.method}
        return recipt

class UPI(Payment):
    def __init__(self):
        self.method = 'UPI'

    def pay(self,amount):
        valid = self.validate(amount)
        if(valid == True):
            print(f'The amount : {amount} is transfered using UPI')
            print(self.recipt(amount))
        else:
            print(f'The amount : {amount} is invalid to transfer')
            return 'No recipt generated'

    def validate(self,amount):
        if(isinstance(amount,int) and 0<amount< 100000):
            return True
        else:
            return False

class Card(Payment):
    def __init__(self):
        self.method = 'Card'

    def pay(self,amount):
        valid = self.validate(amount)
        if(valid == True):
            print(f'The amount : {amount} is transfered using Card')
            print(self.recipt(amount))
        else:
            print(f'The amount : {amount} is invalid to transfer using Card')
            
    def validate(self,amount):
        if( isinstance(amount,int) and 0< amount < 10000000 ):
            return True
        else:
            return False

upi = UPI()
card = Card()

upi.pay(3000)
card.pay(5000)