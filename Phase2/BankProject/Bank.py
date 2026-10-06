import uuid
from pathlib import Path

class Bank():

    USER_DIR = Path(__file__).parent/f'user_accounts'

    def __init__(self,userID):
        self.userID = userID
        self.user_path = Bank.USER_DIR/f'{self.userID}.txt'
        self.user_name = ''

        if self.user_path.exists() and self.user_path.is_file():
            print(f'{self.user_path.exists()}')
            print(f'{self.user_path.is_file()}')

        with open(f'{self.user_path}', 'r') as file:
            lines = file.readlines()
            self.user_name = lines[0].strip()
            self.user_bank = lines[3].strip()
            self.__user_balance_temp = lines[4].strip()
            self.__user_balance = int(self.__user_balance_temp)

    def CheckBalance(self):
        print(f'{self.__user_balance} Is Your Current Balance')

    def CreateAccount(self):
        pass

    def DipositMoney(self):
        print('Diposite successfull')

    def WithDrawMoney(self):
        print('Withdraw successfull')

    def TransferMoney(self):
        print('Service Currently Unavailable')

    def DeleteAccount(self):
        print('Account Delete Successfull')

def HandleChoice(choice,userID):
    user = Bank(userID)
    match choice:
        case 1 : user.CheckBalance()
        case 2 : user.DipositMoney()
        case 3 : user.WithDrawMoney()
        case 4 : user.TransferMoney()
        case _: return print('Unknown Status')

def InAccount(USER_ID):
    user_id = USER_ID

    user = Bank(user_id)

    while 1:
        print('*** Enter What You Want To Do ***')
        choices = {1:'Check Balance',2:'Diposite Money',3:'Withdraw Money',4:'Transfer Money',5:'Exit'}
        for key,value in choices.items():
            print(f'{key} : {value}')

        print('\n')
        choice = int(input('Enter the Option : '))

        if choice > 5 or choice < 1 or type(choice) != int:
            print('Invalid Choice Please Enter From The Available Options')
            continue

        if choice == 5:
            print(f'Bye {user.user_name} Visit Again')
            break

        HandleChoice(choice,user_id)