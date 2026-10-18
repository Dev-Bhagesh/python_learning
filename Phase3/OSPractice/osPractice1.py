import os
from pathlib import Path

cwd = os.getcwd()
print(cwd)
parent = os.path.dirname(cwd)
print(parent)
root = os.path.dirname(parent)
print(root)
print(os.listdir(root))

# root_path = Path(root)
# for item in root_path.rglob('*'):
#     print(item)

phase3 = parent
count = 0
count_py = 0
json_path = []
json_count = 0
for dirpath,dirnames,filenames in os.walk(phase3):
    print(f'Current Directory : {dirpath}')
    print(f'Subdirectrys : {dirnames}')
    print(f'Files : {filenames}')
    count += len(filenames)
    for item in filenames:
        if item.endswith('.json'):
            json_path.append(os.path.join(dirpath,item))
            json_count += 1
    for item in filenames:
        if item.endswith('.py'):
            count_py += 1
    print(f'-'*40)

print(f'Total number of files in Phase3 is : {count}')
print(f'The total number of .py files : {count_py}')

print(f'*'*60)
print(f'Total number of json files : {json_count}')
print(json_path)
