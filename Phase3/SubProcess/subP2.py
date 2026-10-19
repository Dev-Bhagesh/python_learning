import subprocess
from pathlib import Path
# try:
#     subprocess.run(
#         ['python','-c','print(10/0)'],
#         capture_output=True,
#         text=True,
#         check=True
#     )
# except subprocess.CalledProcessError as error:
#     print('Sumthing Went wrong')
#     if error.returncode != 0:
#         print(error.stderr)

file_path = Path('..')/'PathLib'/'hello.py'
script_path = file_path.resolve()

try:
    result = subprocess.run(
        ['python',str(script_path)],
        capture_output=True,
        check=True,
        text=True
    )
    print(result.stdout)
    print('Process run successfully ')
except subprocess.CalledProcessError as error:
    print('Something went wrong')
    print(error.stderr)