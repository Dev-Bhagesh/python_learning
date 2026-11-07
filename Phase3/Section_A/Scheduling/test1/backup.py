import shutil
from pathlib import Path

cwd = Path.cwd()
source_folder = Path(cwd/'Saves').resolve()
destination_folder = Path(cwd/'Backups').resolve()

failed_files = []
success_count = 0
permanent_fails = []
permanent_fails_count = 0

if not destination_folder.exists():
    destination_folder.mkdir(parents=True,exist_ok=True)

for source_file in source_folder.rglob('*.txt'):
    try:
        destination_file = destination_folder/source_file.name

        if source_file.name == 'save_31.txt' or source_file.name == 'save_49.txt':
            raise Exception

        if not destination_file.exists():
            shutil.copy2(source_file,destination_folder)
            print(f'File {source_file.name} Copied successfully')
            success_count += 1
        else:
            print(f'Save Backup alredy exist so skip.. {source_file.name}')
    except Exception as e:
        failed_files.append(source_file)
        print(e)

print('-'*10)
for i in failed_files:
    print(i)

print('-'*10)
for file in failed_files:
    fail_count = 0
    for i in range(1,4):
        try:
            destination_file = destination_folder/file.name

            if file.name == 'save_31.txt':
                raise OSError

            if not destination_file.exists():
                shutil.copy2(file,destination_file)
                print(f'File reattemp success copy')
                success_count += 1
                break
                
        except OSError as e:
            fail_count += 1
            print(f'{i} attempt failed for file {file.name}')

        if fail_count == 3 and fail_count > 0 :
            permanent_fails.append(file)
            permanent_fails_count += 1

print('-'*10)
print(f'Successfull Files Count : {success_count}')
print(f'Permently failed files count : {permanent_fails_count}')
for i in permanent_fails:
    print(i)