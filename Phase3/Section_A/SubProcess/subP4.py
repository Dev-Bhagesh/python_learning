# import subprocess
# try:
#     result = subprocess.run(
#         ['python','-c','print("Pikachu");import time ; time.sleep(5)'],
#         check=True,
#         capture_output=True,
#         text=True,
#         timeout=2,
#     )
#     print(f'output : {result.stdout}')
# except subprocess.TimeoutExpired as error:
#     print(f'output : {error.stdout}')
#     print(f'error : {error.stderr}')

# print('Subprocess completed')

import subprocess

print("Starting subprocess...")

try:
    result = subprocess.run(
        [
            "python", "-c",
            "print('Pikachu', flush=True); import time; time.sleep(5)"
        ],
        check=True,
        capture_output=True,
        text=True,
        timeout=2
    )

    print("Process finished normally!")
    print("Output:", repr(result.stdout))

except subprocess.TimeoutExpired as error:
    print("Process timed out!")
    print("Partial output:", repr(error.stdout))
    print("Partial error:", repr(error.stderr))

except FileNotFoundError as error:
    print("Python executable not found:", error)

print("Parent script continues!")