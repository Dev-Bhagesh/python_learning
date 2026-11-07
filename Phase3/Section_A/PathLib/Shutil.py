from pathlib import Path
import shutil

source = Path('Game2/greninja.txt')
source2 = Path('Game2/delfox.json')
destini = Path('Game2/backup')

destini.mkdir(exist_ok=True)

if source.exists() and not (destini/source.name).exists():
    shutil.copy(source,destini)
else:
    print('File already exists')

if source2.exists() and not (destini/source2.name).exists():
    shutil.move(source2,destini)
else:
    print('File already exists')

source.rename(source.with_name('Greninja_backup.txt'))
new_path = source
print(new_path)
new_path = source.with_name('Greninja_backup.txt')
print(new_path)