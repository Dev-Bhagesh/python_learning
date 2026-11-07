import subprocess
from pathlib import Path

cwd = Path.cwd()
print(cwd)
file = cwd/'demo1.py'

try:
    result = subprocess.run(   
        ['python',str(file)],
        capture_output=True,
        text=True,
        check=False 
    )
    print(f'{result.stdout}')
    print(f'{result.returncode}')
except subprocess.CalledProcessError as error:
    print(f'Something went wrong : {error.stderr}')

except FileNotFoundError as error:
    print('File not found')