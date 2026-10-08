def Choice(choice):
    match choice:
        case 1: pass
        case 2: pass
        case 3: pass
        case _: return True

exit = False
print('=================================================')
print('=*=*= Welcome To The Bhagesh Game World =*=*=')
while 1:
    print('---------------------------------')
    print('| 1 | Create Character          |')
    print('| 2 | Login Into Your Character |')
    print('| 3 | Exit                      |')
    print('---------------------------------')
    User_Choice = input('Enter the Choice : ')
    exit = Choice(User_Choice)
    if exit == True:
        break