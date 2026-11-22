from pathlib import Path
import csv

cwd = Path.cwd()
data_file = Path(cwd/'data'/'Online_Retail.csv').resolve()

def data_cleaning(data_file):
    if not data_file.exists():
        print(f'File does not exist')
        return

    count = 0
    with open(f'{data_file}','r',encoding='utf-8-sig',newline='') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        # print(fieldnames)
        refined_fields = []
        for field in fieldnames:
            refined_fields.append(field.strip())
        print(refined_fields)
        for item in reader:
            count+=1

        print(f'Total number of data rows : {count}')

data_cleaning(data_file)