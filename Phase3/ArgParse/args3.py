import os
from pathlib import Path
import argparse
import sys

protected_roots = [
    Path("C:/Windows"),
    Path("C:/Program Files"),
    Path("C:/Program Files (x86)")
]

parse = argparse.ArgumentParser(description='Validating user input')
parse.add_argument('--file',type=str,required=True,default=None,help='Enter the file path')
arg = parse.parse_args()

user_path = Path(arg.file).resolve()

for root in protected_roots:
    if user_path.is_relative_to(root.resolve()):
        print('Invalid user')
        sys.exit()

print('Valid user')