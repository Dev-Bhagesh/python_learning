from pathlib import Path
import shutil

cwd = Path.cwd().resolve()
txtdir = Path(cwd/'Text').resolve()
jsondir = Path(cwd/'JSON').resolve()
logdir = Path(cwd/'Log').resolve()
otherdir = Path(cwd/'Others').resolve()

try:
    for file in cwd.iterdir():
        if file.exists() and file.is_file() and file.name.endswith('.txt'):
            if not txtdir.exists():
                txtdir.mkdir(parents=True,exist_ok=True)
            print(file)
            destination = Path(txtdir/file.name)
            file.rename(destination)

        elif file.exists() and file.is_file() and file.name.endswith('.json'):
            if not jsondir.exists():
                jsondir.mkdir(parents=True,exist_ok=True)
            print(file)
            # shutil.copy2(file,jsondir)
            destination = Path(jsondir/file.name)
            file.rename(destination)

        elif file.exists() and file.is_file() and file.name.endswith('.log'):
            if not logdir.exists():
                logdir.mkdir(parents=True,exist_ok=True)
            print(file)
            # shutil.copy2(file,logdir)
            destination = Path(logdir/file.name)
            file.rename(destination)

        elif file.suffix != '.py' and file.is_file():
            if not otherdir.exists():
                otherdir.mkdir(parents=True,exist_ok=True)
            print(file)
            shutil.copy2(file,otherdir)

except ValueError as e:
    print(e)