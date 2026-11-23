from pathlib import Path

def GetDataFile(file="Online_Retail"):
    cwd = Path.cwd()
    data_folder = Path(cwd/'data').resolve()
    data_file = Path(cwd/data_folder/f'{file}.csv')
    return data_file
