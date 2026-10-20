import subprocess

try:
    result = subprocess.run(
        ['python','-c','print(" Game Launched! ")'],
        capture_output=True,
        check=True,
        text=True
    )
    print(f'Output : {result.stdout.strip()}')
    print('Launch Successfull!')
except subprocess.CalledProcessError as error :
    print(f'Something went wrong : {error}')