import shutil
from pathlib import Path
file = Path('Game2/Pokemon/temp.txt')

if file.is_file():
    file.unlink()
    print('File Deletion Successfull ')
else:
    print('File does not exist')

file2 = Path('Game2/Empty')

try:
    if file2.is_dir():
        file2.rmdir()
    else:
        print('Folder not Exist')
except OSError:
    print('There are other elements are present in this folder please check before deleting')
file3 = Path('Game2/Pokemon/Trainers')
try:
    if file3.is_dir():
        shutil.rmtree(file3)
    else:
        print('Trainers don\'t exist')
    
except FileNotFoundError:
    print('Trainers Folder not Exists')
