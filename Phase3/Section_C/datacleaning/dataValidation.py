import csv
# from pathlib import Path
from Getdatafile import GetDataFile

file_path = GetDataFile()

def Run():
    if not file_path.exists():
        print('File does not exists')
        return

    negetive = 0
    positive = 0
    zero = 0
    total = 0
    other = 0
    with open(f'{file_path}','r',encoding="utf-8-sig",newline='') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        filtered_fields = []
        for fields in fieldnames:
            filtered_fields.append(fields.strip())

        reader.fieldnames = filtered_fields

        for row in reader:
            total += 1
            # print(row)
            quant = int(row['Quantity'])
            if quant<0:
                negetive += 1
            elif quant == 0:
                zero += 1
            elif quant > 0:
                positive += 1
            else :
                other += 1

    print(f'The Total Number of Records : {total}')
    print(f'The Total Number of Positive Quantity : {positive}')
    print(f'The Total Number of Negative(-) Quantity : {negetive}')
    print(f'The Total Number of Zero Quantity : {zero}')
    print(f'The Total Number of Other Quantity : {other}')

Run()