from pathlib import Path

script_path = Path(__file__).resolve()
file_path = script_path.parent
print(script_path.name)
print(script_path.stem)
print(script_path.suffix)
print(file_path)