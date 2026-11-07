import json
import sys
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='Manage you pokemon save data')
parser.add_argument("--pokemon",type=str,required=True,help='Enter pokemon name')
parser.add_argument('--level',type=int,default=1,help='Enter the pokemon level')
parser.add_argument('--mode',type=str,choices=['easy','normal','hard'],default= 'normal',help='Enter the dificulty level between easy,normal,hard')
parser.add_argument('--shiny',action='store_true',help='include it if you want to add shiny versions')
parser.add_argument('--save-file',type=str,default='save.json',help='Enter the destination path of the file')

args = parser.parse_args()

if args.level > 100 or args.level <= 0 :
    print('Invalid level of Pokemon')
    sys.exit()

print(f'The Pokemon passed is : {args.pokemon}')
print(f'The level of pokemon is : {args.level}')
print(f'The mode of pokemon is : {args.mode}')
print(f'The shiny availabe : {args.shiny}')
print(f'The save file : {args.save_file}')

data = {
    'name':args.pokemon,
    'level':args.level,
    'mode':args.mode,
    'shiny':args.shiny
}

save_path = Path(args.save_file).resolve()
save_path.parent.mkdir(parents=True,exist_ok=True)

if args.save_file :
    with open(f'{args.save_file}','w')as file:
        json.dump(data,file,indent=4)
        print(f'file created successfully')