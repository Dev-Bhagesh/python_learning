import subprocess
import os
from pathlib import Path

cwd = Path.cwd()
file = cwd/'demo1.py'
# print(file)

os.environ['GAME_MODE'] = 'hard'

try:
    result = subprocess.run(
        ['python',str(file)],
        capture_output=True,
        text=True,
        check=True,
    )
    print(f'Output : {result.stdout}')
    print(f'ReturnCode : {result.returncode}')

except subprocess.CalledProcessError as error:
    print(f'Error : {error.stderr}')

except FileNotFoundError as error:
    print('File not found')