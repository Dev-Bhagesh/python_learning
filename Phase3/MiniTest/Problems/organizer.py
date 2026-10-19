from pathlib import Path
import os

def FindDir(direct):
    dire = direct

    while True:
        if dire.parent == dire:
            return None
        
        root = dire
        for item in root.iterdir():
            if item.is_dir() and item.name == 'Organizer':
                return item
        dire = dire.parent

cwd = Path.cwd()
Org_path = FindDir(cwd)

if Org_path is not None:
    if Org_path.exists() and Org_path.is_dir():
        for item in Org_path.iterdir():
            if item.exists() and item.is_file():
                if item.name.endswith('.json'):
                    folder = 'Data'
                    Org = Org_path/folder
                    Org.mkdir(parents=True,exist_ok=True)
                    # item_path = item
                    destination = Org/item.name
                    item.rename(destination)
                elif item.name.endswith('.png') or item.name.endswith('.jpg') or item.name.endswith('.jpeg'):
                    folder = 'Images'
                    Org = Org_path/folder
                    Org.mkdir(parents=True,exist_ok=True)
                    destination = Org/item.name
                    item.rename(destination)
                elif item.name.endswith('.txt'):
                    folder = 'Text'
                    Org = Org_path/folder
                    Org.mkdir(parents=True,exist_ok=True)
                    destination = Org/item.name
                    item.rename(destination)
                else:
                    folder = 'Others'
                    Org = Org_path/folder
                    Org.mkdir(parents=True,exist_ok= True)
                    destination = Org/item.name
                    item.rename(destination)
else:
    print('Directry not found')