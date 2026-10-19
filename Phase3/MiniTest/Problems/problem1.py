# problem 1
from pathlib import Path
import os

current_dir = Path.cwd()
print(current_dir)
script = Path(__file__)
script_name, script_stem, script_parent, script_suffix = script.name , script.stem , script.parent, script.suffix

print(script_name)
print(script_suffix)
print(script_stem)
print(script_parent)

# full_path = current_dir.joinpath(script_name)
# print(full_path)

if script.exists():
    print(f'{script} : exists')
    if script.is_file():
        print(f'{script} is a file ')
    else:
        print(f'{script} : is not a file')
else :
    print(f'{script} : does not exists')

if current_dir.exists():
    if current_dir.is_dir():
        print(f'{current_dir} : is dir')
    else:
        print(f'{current_dir} : is not a dir')
else:
    print(f'{current_dir} does not exists')

print('-'*30)

dir_count = 0
file_count = 0
current_dir_parent = current_dir.parent
list = []
count = 0
for item in current_dir_parent.rglob('*'):
    if item.is_file():
        file_count += 1
    elif item.is_dir():
        dir_count += 1

    list.append(item)
    count += 1
print(list)
print(f'Total number of entrys is : {count}')

count = 0
direct_childs = []
for item in current_dir_parent.iterdir():
    direct_childs.append(item)
    count += 1

print(f'Direct childrens of {current_dir_parent}')
print(direct_childs)
print(f'Count of direct children : {count}')

print(f'Directorys : {dir_count}')
print(f'Files : {file_count}')
print('-'*30)

print(os.listdir(script_parent))