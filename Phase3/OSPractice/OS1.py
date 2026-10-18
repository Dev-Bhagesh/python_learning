import os

cwd = os.getcwd()
print(cwd)

try:
    cwd2 = os.getcwd()
    parent = os.path.dirname(cwd2)
    print(parent)
    pathfile = os.path.join(parent,'PathLib')
    print(pathfile)
    files = os.listdir(pathfile)
    print(files)
except FileNotFoundError:
    print("Folder don't exist")