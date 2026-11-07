from pathlib import Path

file_path = Path('Game2')

if not file_path.is_dir():
    print('Folder not exist')
else:
    try:
        for file in file_path.rglob('*.json'):
            print(file)

        print('\n')

        for file in file_path.rglob('*.txt'):
            print(file)

        print('\n')
        count = 0
        total_size = 0
        for file in file_path.rglob('*'):
            if file.is_file() and file.stat().st_size > 100:
                print(file)
                total_size += file.stat().st_size
                count += 1

        print(f'The total files who are larger then 100 bytes : {count}')
        print(f'Total size of all files : {total_size}')
    except FileNotFoundError:
        print('Files Not found')