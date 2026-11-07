import os
username = os.getenv('USERNAME')
home = os.getenv('USERPROFILE')
temp = os.getenv('TEMP')
print(username)
print(home)
print(temp)

print(os.getenv('pokemon','red'))
print(os.getenv('league','jhoto'))

# Environ

os.environ['pokemon'] = 'Charizard'
print(os.environ['pokemon'])
print(os.getenv('pokemon','pikachu'))
# print(os.environ['pokemon'])
print(os.environ.get('pokemon','mewtow'))