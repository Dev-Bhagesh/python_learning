import string
import random
from pathlib import Path
import Bank

class Login:
    USER_DIR = Path(__file__).parent/'user_accounts'
    USER_DIR.mkdir(exist_ok=True)
    def __init__(self):
        pass

    def CreateAccount(self):

        user_name = input('Enter the Name : ')
        chCapIn = random.choice(string.ascii_uppercase)
        chSmlIn = random.choice(string.ascii_lowercase)
        chRand = random.choice(string.ascii_letters)
        chNumIn = random.randint(1,10000)

        capital_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        # small_letters = list(string.ascii_lowercase)
        small_letters = [chr(i) for i in range(ord('a'),ord('z')+1)]

        user_id = chCapIn + chSmlIn + str(chNumIn) + chRand

        file1 = Login.USER_DIR/f'{user_id}.txt'

        exist = True
        while exist:
            flage = True
            if file1.exists() and file1.is_file():
                user_name = input('Enter the Name : ')
                chCapIn = random.choice(string.ascii_uppercase)
                chSmlIn = random.choice(string.ascii_lowercase)
                chRand = random.choice(string.ascii_letters)
                chNumIn = random.randint(1,10000)
                    
                capital_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
                small_letters = list(string.ascii_lowercase)     
                # user_id = capital_letters[chCapIn] + small_letters[chSmlIn] + str(chNumIn)
                user_id = chCapIn + chSmlIn + str(chNumIn) + chRand
                file1 = Login.USER_DIR/f'{user_id}.txt'
                flage = False
            if flage == True:
                exist = False


        file = Login.USER_DIR/f'{user_id}.txt'

        if file.exists():
            print('User Alredy Exist')
            return

        BanksList = {1:'IDBI',2:'SBI',3:'ICICI',4:'HDFC'}
        for key,value in BanksList.items():
            print(f'{key} . {value}')

        bank = int(input('Enter The Bank Number : '))
        password = int(input('Enter the passowrd : '))
        dipositeAmount = int(input('Enter Diposite Amount (Minimum 500) : '))

        if bank in BanksList and user_name and user_name != '' and dipositeAmount >= 500:
            user_account = Login.USER_DIR/f'{user_id}.txt'
            with open(user_account,'x') as file:
                file.write(f'{user_name}\n')
                file.write(f'{user_id}\n')
                file.write(f'{password}\n')
                file.write(f'{BanksList[bank]}\n')
                file.write(f'{dipositeAmount}\n')
            print(f'The Account Is Created At Bank {BanksList[bank]}')
        print(f'Please Note the Unique ID of Your Account ** {user_id} **')

    def LoginIntoAccount(self):
        user_id = input('Enter the user ID : ')
        user_account = Login.USER_DIR/f'{user_id}.txt'
        if user_account.exists() and user_account.is_file():
            user_account_login_name = input('Enter the name of the User :')
            user_account_login_password = int(input('Enter the password :'))
            user_password = ''
            user_name = ''

            with open(f'{user_account}','r') as file:
                lines = file.readlines()
                user_name = lines[0].strip()
                print(f'{user_name}')
                user_password = lines[2].strip()
                print(f'{user_password}')

            if user_account_login_name == user_name and str(user_account_login_password) == user_password:
                print(f'Login Successfull Welcome {user_account_login_name}')

                Bank.InAccount(user_id)
            
        else :
            print('User not Exist')

