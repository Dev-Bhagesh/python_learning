import subprocess
result = subprocess.run(
    ['python','--version'],
    capture_output=True,
    text=True
)

print(result.stdout)
# print(result.returncode)

result2 = subprocess.run(
    ['python','-c','print("pikachu used thunder")'],
    capture_output = True,
    text=True
)

print(result2.stdout)
print(result2.returncode)

result3 = subprocess.run(
    ['python','-c','print(10/0)'],
    capture_output = True,
    text=True,
    check=True
)

if result3.returncode != 0 :
    
    print('Something went wrong')
    print(result3.stderr)
else:
    print(result3.stdout)
    print(result3.returncode)
