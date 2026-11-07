import os
from pathlib import Path
import json
import argparse

parse = argparse.ArgumentParser(description='Enter all values correctly')
parse.add_argument('--save-file',type=str,default=None,help='Enter path of save file')
parse.add_argument('--pokemon',type=str,default=None,help='Enter name of pokemon')
parse.add_argument('--level',type=int,default=1,help='Enter the level between 1-100')
parse.add_argument('--mode',type=str,default='normal',choices=['easy','normal','hard'],help='Enter mode from easy,normal,hard')
parse.add_argument('--shiny',action='store_true',help='Include if you want shiny version')

arg = parse.parse_args()

pokemon = {
    'pokemon':arg.pokemon,
    'level':arg.level,
    'mode':arg.mode,
    'shiny':arg.shiny,
}

# os.environ['POKEMON_PATH'] = 'backup/poke2.json'
env = os.getenv('POKEMON_PATH')
save_path = Path(arg.save_file or env or 'backup/save.json')

save_path.parent.mkdir(parents=True,exist_ok=True)

with open(f'{save_path}','w') as file:
    json.dump(pokemon,file,indent=4)