import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--pokemon",type=str,required=True)
parser.add_argument('--level',type=int,default=1)
parser.add_argument('--mode',type=str,choices=['noraml','medium','hard'],default= 'normal')
parser.add_argument('--shiny',action='store_true')
parser.add_argument('--save-file',type=str,default='save.json')

args = parser.parse_args()
print(f'The Pokemon passed is : {args.pokemon}')
print(f'The level of pokemon is : {args.level}')
print(f'The mode of pokemon is : {args.mode}')
print(f'The shiny availabe : {args.shiny}')
print(f'The save file : {args.save_file}')