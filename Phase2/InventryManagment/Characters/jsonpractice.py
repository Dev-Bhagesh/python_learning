import json

try:
    with open('profile.json','r') as file:
        profiles = json.load(file)

except FileNotFoundError:
    profiles = []

while 1 :
    name = input('Enter the name : ')
    age = int(input('Enter the age : '))
    role = input('Enter the role : ')
    exit = int(input("Enter 1 to exit or 0 to continue : "))
    
    if exit == 1:
        break
    
    profiles.append(profile)
    profile = {
        'name' : name,
        'age' : age,
        'role' : role
    }

with open('profile.json','w') as file:
    json.dump(profiles,file,indent=4)
    print('json created successfully')