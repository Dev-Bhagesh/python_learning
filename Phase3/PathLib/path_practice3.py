# Creation of folders and files
from pathlib import Path
folder = Path('Game2')
print(folder)
print(folder.exists())
print(folder.is_dir())
print(folder.is_file())
print('\n')
try:
    folder.mkdir()
    print('Folder Created')
except FileExistsError:
    print('Folder alredy Exists')
print(folder)
print(folder.exists())
print(folder.is_file())
print(folder.is_dir())

pokemon = Path('Game2/Pokemon/Teams')
pokemon.mkdir(parents=True,exist_ok=True)

print(pokemon.exists())
print(pokemon)

pokemon2 = Path('Game2/Pokemon/Trainers/Kanto')
pokemon2.mkdir(parents=True,exist_ok=True)
print(pokemon2)
print(pokemon2.exists())