import os
cwd = os.getcwd()
path = os.path.join(cwd,'OS1.py')

if os.path.exists(path) and os.path.isfile(path):
    basename = os.path.basename(path)
    print(f'Basename of the file : {basename}')
    print(os.path.splitext(os.path.basename(path))[0])
    print(os.path.splitext(os.path.basename(path))[1])
    print(os.path.getsize(path))
else:
    print('File does not exist')