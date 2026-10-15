# Joining Paths
from pathlib import Path
folder = Path('Game')
file_path = folder/f'data.txt'

# print(folder)
# print(file_path)
# print(file_path.resolve())
# print(file_path.exists())
# print(file_path.is_file())

path1 = Path('Game/data.txt')
print(path1.name)
print(path1.stem)
print(path1.suffix)
print(path1.parent)