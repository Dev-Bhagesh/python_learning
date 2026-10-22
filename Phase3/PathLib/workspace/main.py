from pathlib import Path
import os

workspace = Path(__file__).resolve().parent
print(workspace)
target = Path(workspace/'missing').resolve()
# target = Path(__file__).resolve()
print(target)

count = 0
try:
    target.relative_to(workspace)
    # if target.exists() and target.is_dir():
    #     for item in target.iterdir():
    #         if item.is_file() and item.suffix == '.log':
    #             print(f'{item}')
    #             count += 1
    #     if count <= 0 :
    #         print('There are no log files')
    #     else:
    #         print(f'Total number of Log files : {count}')
    # elif target.exists() and target.is_file():
    #     print('This is a file not a folder ')
    # else:    
    #     print('The folder does not exist')

    if target.exists():
        if target.is_dir():
            for item in target.iterdir():
                if item.is_file() and item.suffix == '.log':
                    print(f'{item}')
                    count += 1
            if count > 0:
                print(f'Total count of .log fils : {count}')
            else:
                print('No log files found')
        else:
            print('The path is pointing to a file not directry')
    else:
        print('The path doest exist')
        
except ValueError:
    print('Folder is outside the workspace')
