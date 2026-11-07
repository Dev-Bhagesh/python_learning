from pathlib import Path

folder = Path.cwd()
savesFolder = Path(folder/'Saves')

if savesFolder.exists() == False:
    savesFolder.mkdir()

for i in range(1,101):
    file_path = savesFolder/f'save_{i}.txt'
    file_path.touch()
    with open(f'{file_path}','w')as file:
        file.write(f'This is file number {i}')

print('100 files created successfully')