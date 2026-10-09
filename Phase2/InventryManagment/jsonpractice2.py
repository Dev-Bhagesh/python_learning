import json

with open('profile.json','r') as file:
    profiles = json.load(file)

for profile in profiles:
    print(f'Name : {profile["name"]}')
    print(f'Age  : {profile["age"]}')
    print(f'Role : {profile["role"]}')
    print('-' * 25)