import shutil
from pathlib import Path
import logging

logging.basicConfig(
    filemode='a',
    filename='backup.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s = %(message)s'
)

cwd = Path(__file__).parent.resolve()
print(cwd)
dest_folder = Path(cwd/'backup')
print(dest_folder)
files = ['pika.json','bulba.json','charm.json']
for file in files:
    try:
        # if dest_folder.exists() == False:
        dest_folder.mkdir(parents=True,exist_ok=True)
        desti_file = Path(dest_folder/file)
        source_file = Path(cwd/file)
        if not source_file.is_file():
            logging.warning(f'The source file {source_file} does not exist')
        elif desti_file.exists():
            logging.info(f'The backup file of {file} alredy exists so it is skipped')
        else:
            print(desti_file)
            shutil.copy(f'{file}',f'{desti_file}')
            logging.info(f'The file is copied')
    except FileNotFoundError:
        logging.warning(f'{file} not found')
    except PermissionError:
        logging.warning(f'{file} have no permission to copy')