import shutil
from pathlib import Path

parent_folder = Path(__file__).parent.resolve()
# print(parent_folder)

pokemon_folder = Path(parent_folder/'pokemon_manager').resolve()
# print(pokemon_folder)

Exist = False
save_num = 0
copy_exist = False
save_json = Path('')
backup_folder = Path('')
try:
    pokemon_folder.relative_to(parent_folder)
    if pokemon_folder.exists() and pokemon_folder.is_dir():
        
        for item in pokemon_folder.glob('*.json'):
            if item.stem == 'save':
                save_json = Path(item)
        
        for item in pokemon_folder.iterdir():
            if item.is_dir() and item.name == 'backup':
                backup_folder = Path(item)

        for item in backup_folder.glob('*.json'):
            if item.is_file() and item.stem == 'save' and item.suffix == '.json':
                copy_exist = True

    for item in backup_folder.iterdir():
        if item.is_file() and item.suffix == '.json':
            # if len(item.stem) == 4:
            stem3 = item.stem.split('_')
            if len(stem3) == 2 and stem3[0] == 'save':
                save_num = max(save_num,int(stem3[1]))
                print(stem3[0])
                print(stem3[1])
                print(save_num)

            # stem1 = item.stem
            # stem2 = str(stem1)
            # stem3 = stem2.split('_')
            # print(stem3[0])
            # print(stem3[1])

            # if stem3[0] == 'save':
            #     save_num = int(stem3[1])
            
            # if stem3[0] == 'save':
            #     save_num = int(save_str.split('_')[1])
            #     print(save_num)

            # if item.is_file() and item.suffix == '.json':
            #     print('Save file alredy Exist')
            #     copy_exist = True

    # print(save_json)
    # print(backup_folder)

    if save_json.suffix == '.json' and backup_folder.name == 'backup':
        if copy_exist != True:
            shutil.copy(save_json,backup_folder)
            print('Save file copyd to backup folder successfully')
        else:
            number = save_num + 1
            save_json_copy = save_json.with_stem(save_json.stem + '_' + str(number))
            print(save_json_copy)
            destination = backup_folder/save_json_copy.name
            shutil.copy(save_json,destination)
    else:
        print('Something is not right')

except ValueError:
    print('The folder is outside the limit')

except PermissionError:
    print('No save.json file found')