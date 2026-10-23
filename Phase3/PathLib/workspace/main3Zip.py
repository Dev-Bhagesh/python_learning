import shutil
from pathlib import Path

parent = Path(__file__).parent.resolve()
print(parent)
Poke_folder = Path(parent/'pokemon_manager').resolve()
print(Poke_folder)
print(Poke_folder.exists())
source_folder = Path(Poke_folder/'baka').resolve()
destination = Path(Poke_folder/'PokeZip').resolve()

shutil.make_archive(
    str(destination),
    "zip",
    root_dir=str(source_folder)
)