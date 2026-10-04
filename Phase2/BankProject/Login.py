
import random
from pathlib import Path

class Login:
    USER_DIR = Path(__file__).parent/'user_accounts'
    USER_DIR.mkdir(exist_ok=True)
    def __init__(self):
        pass

    def CreateAccount(self):

        user_name = input('Enter the Name : ')
        user_id = random.randint(1,101)

        file = Login.USER_DIR/f'{user_id}.txt'

        if file.exists():
            print('User Alredy Exist')
            return

        dictn = {1:'IDBI',2:'SBI',3:'ICICI',4:'HDFC'}
        for key,value in dictn.items():
            print(f'{key} . {value}')

        bank = int(input('Enter The Bank Number : '))
        password = int(input('Enter the passowrd : '))
        dipositeAmount = int(input('Enter Diposite Amount (Minimum 500) : '))

        if bank in dictn and user_name and user_name != '' and dipositeAmount >= 500:
            user_account = Login.USER_DIR/f'{user_id}.txt'
            with open(user_account,'w') as file:
                file.write(f'{user_name}')
                file.write(f'{user_id}')
                file.write(f'{password}')
                file.write(f'{bank}')
                file.write(f'{dipositeAmount}')

    def LoginIntoAccount(self):
        user_id = input('Enter the user ID : ')
        user_account = Login.USER_DIR/f'{user_id}.txt'
        if user_account.exists() and user_account.is_file():
            print('User Exist')
        else :
            print('User not Exist')

