import csv
from pathlib import Path
import openpyxl

cwd = Path.cwd()
data_file = Path(cwd/'data'/'Online Retail.xlsx').resolve()

workbook = openpyxl.load_workbook(
    f'{data_file}',
    read_only = True,
    data_only = True
)

sheet = workbook.active

destination = Path(cwd/'data'/'Online_Retail.csv').resolve()

with open(f'{destination}','w',newline='',encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerows(sheet.iter_rows(values_only=True))

workbook.close()