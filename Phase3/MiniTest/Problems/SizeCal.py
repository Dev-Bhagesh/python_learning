from pathlib import Path
import os
import organizer

inpt = input('Enter the Path : ')
cwd = Path.cwd()
files_size = 0
file_counts = 0

user_path = Path(inpt)

if user_path.exists():
    if user_path.is_dir():
        # for dirpaths,dirnames,filenames in os.walk(user_path):
        #     for item in filenames:
        #         temp = Path(dirpaths)/item
        #         print(item)
        #         print(f'File Path : {temp} ')
        #         print(f'file Size : {temp.stat().st_size}')
        #         file_counts += 1
        #         files_size += temp.stat().st_size

        for item in user_path.rglob('*'):
            if item.is_file():
                files_size += item.stat().st_size
                file_counts += 1

        print(file_counts)
        print(f'Total Size : {files_size/1024:.2f} KB')
    elif user_path.is_file():
        print('Its a file Please Enter a folder path')

else:
    file_path = organizer.FindDir(cwd,inpt)

    if file_path is not None:
        if file_path.exists() and file_path.is_dir():
            # for dirpaths,dirnames,filenames in os.walk(file_path):
            #     for item in filenames:
            #         temp = Path(dirpaths)/item
            #         files_size += temp.stat().st_size
            #         file_counts += 1
            
            for item in file_path.rglob('*'):
                if item.is_file():
                    file_counts += 1
                    files_size += item.stat().st_size

        print(file_counts)
        print(f'Total Size : {files_size/1024:.2f} KB')
    else:
        print('Folder does not exist')