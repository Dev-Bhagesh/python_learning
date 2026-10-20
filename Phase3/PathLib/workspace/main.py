from pathlib import Path
import os

workspace = Path(__file__).resolve().parent
print(workspace)
target = Path(workspace/'pokemon_manager').resolve()
print(target)

try:
    target.relative_to(workspace)
    if target.exists() and target.is_dir():
        for item in target.iterdir():
            if item.is_file() and item.suffix == '.log':
                print(f'The file would be deleted : {item}')
    else:
        print('The folder does not exist')
except ValueError:
    print('Folder is outside the workspace')