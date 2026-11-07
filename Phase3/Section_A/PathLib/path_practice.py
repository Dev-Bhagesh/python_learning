# Using Pathlib and understanding paths
from pathlib import Path
file_path = Path('data.txt')
folder_path = Path('Game')
# print(file_path)
# print(folder_path)
# print(type(file_path))
# print(type(folder_path))
# print(file_path.exists())
# print(folder_path.exists())

print(file_path.is_file())
print(file_path.is_dir())
print('\n')

print(folder_path.is_file())
print(folder_path.is_dir())
print('\n')

print(file_path.resolve())
print(folder_path.resolve())
print('\n')