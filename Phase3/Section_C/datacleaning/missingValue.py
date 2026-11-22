import json
import csv
from pathlib import Path
cwd = Path.cwd()
data_file = Path(cwd/'data'/'Online_Retail.csv').resolve()

def missValue(data_file):
    if not data_file.exists():
        print('File not found')
        return
    refined_fields = [] 
    with open(f'{data_file}','r',encoding='utf-8-sig',newline='') as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames

        for field in fields:
            refined_fields.append(field.strip())

        reader.fieldnames = refined_fields

        obj = {field:0 for field in refined_fields}
        count = 0
        for row in reader:
            count += 1
            for field in refined_fields:
                if(row[field].strip() == '' or row[field].strip() == None):
                    obj[field] += 1

        percentage = {field :(obj[field]/count) * 100 for field in obj}
        print(json.dumps(obj))
        for field,value in percentage.items():
            print(f'{field}:{value:.2f}%')

missValue(data_file)