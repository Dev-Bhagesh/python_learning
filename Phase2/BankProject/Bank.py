import uuid

class Bank():
    def __init__(self):
        pass

exit = True
while(exit):
    print('===== Welcome to the CLI Bank System =====')
    print('1. Create Account \n2. View Your Account Info \n3. Login to Your Account \n4.Exit')
    inpt = int(input('Select the Choice : '))

    if inpt == 4 :
        exit = True
        print('=== Exiting the CLI Bank System Please Come Again ===')
        break

    