import uuid
from pathlib import Path

class Bank():

    USER_DIR = Path(__file__).parent/f'user_accounts'

    def __init__(self,userID):
        self.userID = userID
        self.user_path = Bank.USER_DIR/f'{self.userID}.txt'
        self.user_name = ''

        # if self.user_path.exists() and self.user_path.is_file():
        #     print(f'{self.user_path.exists()}')
        #     print(f'{self.user_path.is_file()}')

        with open(f'{self.user_path}', 'r') as file:
            lines = file.readlines()
            self.user_name = lines[0].strip()
            self.user_bank = lines[3].strip()
            self.__user_balance_temp = lines[4].strip()
            self.__user_balance = int(self.__user_balance_temp)

    def CheckBalance(self):
        print(f'{self.__user_balance} Is Your Current Balance')
        print('----------------------------------------------------------')

    def CreateAccount(self):
        pass

    def DipositMoney(self):
        amount = int(input('Enter the Amount you want to Diposit : '))
        if amount > 0 : 
            with open(f'{self.user_path}','r') as file:
                lines = file.readlines()

            bal_amount = int(lines[4].strip())
            total_amount = bal_amount + amount
            final_diposit_amount = str(total_amount)
            lines[4] = f'{final_diposit_amount}\n'

            with open(f'{self.user_path}','w') as file:
                file.writelines(lines)
            print('Diposite successfull')
            print('-------------------------------------------------------')
        else:
            print('Invalid Amount')

    def WithDrawMoney(self):
        with_amount = int(input('Enter the Withdraw Amount : '))
        if with_amount < self.__user_balance and with_amount > 0:
            with open(f'{self.user_path}','r') as file:
                lines = file.readlines()

            bal_amount = int(lines[4].strip())
            final_amount = bal_amount - with_amount
            lines[4] = str(final_amount)
            with open(f'{self.user_path}','w') as file:
                file.writelines(lines)
            print('Withdraw successfull')
        else:
            print('Insufficiant Balance')

    def TransferMoney(self):
        print('-----------------------------------------------------------')
        recivers_id = input('Enter the Recivers ID : ')
        recivers_path = self.USER_DIR/f'{recivers_id}.txt'
        if recivers_path.exists() and recivers_path.is_file():
            transfer_amount = int(input('Enter the Amount to be transfered : '))
            if transfer_amount <= self.__user_balance and transfer_amount > 0:
                with open(f'{self.user_path}','r') as file:
                    sender_lines = file.readlines()
                    sender_bal = int(sender_lines[4].strip())
                    remaining_sender_bal = sender_bal - transfer_amount
                    sender_lines[4] = str(remaining_sender_bal)

                with open(f'{recivers_path}','r') as file:
                    reciver_lines = file.readlines()
                    reciver_bal = int(reciver_lines[4].strip())
                    added_bal = reciver_bal + transfer_amount
                    reciver_lines[4] = str(added_bal)

                with open(f'{recivers_path}','w')as file:
                    file.writelines(reciver_lines)

                with open(f'{self.user_path}','w') as file:
                    file.writelines(sender_lines)

                print(f'Money transfered Successfully to accoount {recivers_id}')
            else:
                print('Insufficient amount')
        else:
            print('Recivers Account Not Found')
        print('---------------------------------------------------------------------')

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