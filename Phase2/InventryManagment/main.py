import Login

def Choice(choice):
    login = Login.FirstLayer()
    match choice:
        case 1:
            retu = login.CreateCharacter() 
            return retu
        #login.CreateCharacter()
        case 2:
            retu = login.LogintoCharacter()
            return retu
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
    try:
        User_Choice = int(input('Enter the Choice : '))
        if User_Choice == 3 or User_Choice == '':
            print('='*25+' Plese Visit Us Again '+'='*25)
            break
        choice = Choice(User_Choice)
        if choice == 1:
            print('Servers are Currupted Right now visit later Thank you ')
            break
    except ValueError:
        print('Invalid input please Enter a Number from given choice ')