import Login

def Choice(choice):
    login = Login.FirstLayer()
    match choice:
        case 1: login.CreateCharacter() 
        #login.CreateCharacter()
        case 2: login.LogintoCharacter()
        case 3: pass
        case _: return 1

exit = 0
print('=================================================')
print('=*=*= Welcome To The Bhagesh Game World =*=*=')
while 1:
    print('---------------------------------')
    print('| 1 | Create Character          |')
    print('| 2 | Login Into Your Character |')
    print('| 3 | Exit                      |')
    print('---------------------------------')
  
    User_Choice = int(input('Enter the Choice : '))
    if User_Choice == 3:
        break
    Choice(User_Choice)