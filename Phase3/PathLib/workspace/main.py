from pathlib import Path
import os

workspace = Path(__file__).resolve().parent
print(workspace)
target = Path(workspace.parent/'pokemon_manager').resolve()
print(target)

count = 0
try:
    target.relative_to(workspace)
    if target.exists() and target.is_dir():
        for item in target.iterdir():
            if item.is_file() and item.suffix == '.log':
                print(f'{item}')
                count += 1
        if count <= 0 :
            print('There are no log files')
        else:
            print(f'Total number of Log files : {count}')
    else:
        print('The folder does not exist')
        
except ValueError:
    print('Folder is outside the workspace')
