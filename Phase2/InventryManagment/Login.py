import json
import os
import CharClass
from pathlib import Path

class FirstLayer():
    CHAR_DIR = Path(__file__).parent/'Characters'

    def CreateCharacter(self):
        name = input('Enter the Name Of the Character : ')
        age = int(input('Enter the age : '))
        rolesList = ['Archer','Knight','Swards Man','Wizard']
        print('Chose A Character Type ')
        print('-' * 25)
        i = 1
        for role in rolesList:
            print(f'{i} : {role} ')
            i += 1
        print('-' * 25)
        roleChoice = int(input('Enter the Choice for Role : '))
        role = rolesList[roleChoice-1]

        Password = input('Enter the password : ')
        Password = Password.strip()
        Password = Password.replace(" ","")

        print('Inverntry Will Be Available After Creation And Login Of The Character')

        
        Char_path = FirstLayer.CHAR_DIR/f'characters.json'
        if Char_path.exists() and Char_path.stat().st_size > 0:
            with open(Char_path, 'r') as file:
                Profiles = json.load(file)
                lastProfile = Profiles[-1]
                temp = lastProfile['id']
                id = temp + 1
        else:
            Profiles = []
            id = 1

        profile = {
            'id' : id,
            'password' : Password,
            'name' : name,
            'age' : age,
            'role' : role,
            'inventory' : [],
        }

        Profiles.append(profile)

        os.makedirs(os.path.dirname(Char_path),exist_ok=True)

        with open(f'{Char_path}','w') as file:
            json.dump(Profiles,file,indent=4)

        print(f'Character Creation Successfull Your ID is : -> {id} <- Please Not This And The Password')
       

    def LogintoCharacter(self):
        print('-'*25,' Login ','-'*25)
        id = int(input('Enter the id : '))
        name = input('Enter the name : ')
        password = input('Enter the password : ')

        Char_path = FirstLayer.CHAR_DIR/f'characters.json'

        try:
            with open(f'{Char_path}','r') as file:
                Profiles = json.load(file)
        except FileNotFoundError:
            print('Internal Database Error Please Try Later... ')
            return
        

        Profile = next((profile for profile in Profiles if int(profile['id']) == id),None)

        if Profile:
            if Profile['name'] == name and Profile['password'] == password :
                CharClass.SecondLayer(Profile)
        else :
            print('Wrong Credentials')
            return