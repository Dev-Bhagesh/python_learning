from Login import Login
def EnterSystem(choice):
    match choice:
        case 1 :
            login = Login()
            login.CreateAccount()

        case 2 :
            login = Login()
            login.LoginIntoAccount()

        case _: return False

while 1:
    print('===== Welcome to CLI Bank System =====')
    print('1. Create Account\n2. Login\n3. Exit\n ')
    choice = int(input('Enter the Choice : '))

    if choice == 3:
        print('=== Visit Again ===')
        break
    else:
        if EnterSystem(choice) == False: 
            print('=== Visit Again ===')
            break
    