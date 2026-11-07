from pathlib import Path
import psutil

def process_files(files):
    content = files.read_text(encoding='utf-8')
    if not content.strip():
        raise ValueError('File is empty')

    print(f'{files.name} : processed successfulyy')

cwd = Path.cwd()
folder_path = Path(cwd/'Saves')

if folder_path.exists() and folder_path.is_dir():
    for file in folder_path.rglob('*.txt'):
        try:
            if file.is_file():
                process_files(file)
        except Exception as e:
            print(e)    