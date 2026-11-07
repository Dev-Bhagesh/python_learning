import shutil
from logging.handlers import RotatingFileHandler
import logging
from pathlib import Path
import psutil

cwd = Path.cwd()
pokefolder = Path(cwd/'Pokesave')
destination = Path(cwd/'Pokedest')
try:
    if pokefolder.exists() == False:
        raise FileNotFoundError
    
    file_count = 0
    for items in pokefolder.rglob('*.txt'):
        if items.is_file():
            file_count += 1

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(
        filename='Pokesave.log',
        maxBytes=1024*1024,
        backupCount=3,
        encoding='utf-8'
    )

    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    if destination.exists() == False:
        destination.mkdir()

    success_count = 0
    failure_count = 0
    for file in pokefolder.rglob('*.txt'):
        try:
            if file.is_file():
                shutil.copy(file,destination)
                print('Success')
                logger.info(f'The File {file.name} is copyd successfully')
                success_count += 1

        except FileNotFoundError as error:
            failure_count += 1
            logger.error(f'File not found')
            print(f'File not found')
        except PermissionError as error :
            failure_count += 1
            logger.error(f'Not have permission')
            print(f'Not have permission')
        except IsADirectoryError as error :
            failure_count += 1
            logger.error(f'Trying to copy a directry')
            print(f'Trying to copy a directry')
        except OSError as error:
            failure_count += 1
            logger.error(f'OS Error')
            print(f'OS Error')
        except psutil.Error:
            failure_count += 1
            logger.error(f'Psutil erro')
            print(f'Psutil erro')

    print(f'Success Count : {success_count}')
    print(f'Failure Count : {failure_count}')
except FileNotFoundError:
    print(f'File not found error')