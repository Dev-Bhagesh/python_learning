import os
path = os.getcwd()
# print(path)
# print(os.path.basename(path))
# print(os.path.dirname(path))
# print(os.path.splitext(path))

# print(os.path.exists(path))
# print(os.path.isfile(path))
# print(os.path.isdir(path))

path2 = os.path.join(path,'OS2.py')
print(os.path.exists(path2))
print(os.path.isfile(path2))
print(os.path.isdir(path2))

if os.path.exists(path2):
    print(os.path.getsize(path2))