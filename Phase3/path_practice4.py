from pathlib import Path

# file_path = Path('Game')/'progress.txt'
# try:
#     file_path.touch()
#     print("Creation successfull")
# except FileNotFoundError:
    
#     file_path.parent.mkdir()
#     file_path.touch()
#     print('Folder Created and file also created')

file_path = Path('Project')/'Game3'/'save.txt'
file_path.parent.mkdir(parents=True,exist_ok=True)
done = file_path.touch()

if file_path.exists():
    print('success')
else:
    print('Something went wrong')

files_in_folder = []
files = []
dirs = []
unknown = []
file_path2 = Path('Game')

print('All Elements In The Game')
for item in file_path2.iterdir():
    files_in_folder.append(item)
    print(item)
    if item.is_file() == True:
        files.append(item)
    elif item.is_dir() == True:
        dirs.append(item)
    else:
        unknown.append(item)

print('\n')
print('All Files Present In Game')
for item in files:
    print(item)
print('\n')

print('All Directoris In Game')
for item in dirs:
    print(item)
print('\n')

print('All Unknown Files')
for item in file_path2.iterdir():
    if item.suffix == '.txt':
        print(item)