from pathlib import Path

file_path = Path('Game')
file_count = 0
dir_count = 0
txt_count = 0

for item in file_path.iterdir():
    if item.is_file() :
        file_count += 1
        if item.suffix == '.txt':
            txt_count += 1
    elif item.is_dir() :
        dir_count += 1

print(f'TXT file count {txt_count}')
print(f'Dirctory count {dir_count}')
print(f'File count {file_count}')