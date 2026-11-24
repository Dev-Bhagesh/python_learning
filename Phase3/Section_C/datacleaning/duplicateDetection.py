import csv
from Getdatafile import GetDataFile

def FindDuplicatesByName():
    records = [
    [1001, "Pikachu", 25],
    [1002, "Charmander", 15],
    [1003, "pikachu", 30],
    [1004, "Bulbasaur", 20],
    [1005, "PIKACHU", 35]
]

    seeNames = set()
    seen = set()
    duplicate = []

    for item in records:
        current = item[1].lower()
        if current in seeNames:
            # duplicate.add(tuple(item))
            duplicate.append(item)
        else:
            seen.add(tuple(item))
            seeNames.add(current)

    print('Duplicate Pokemon : ')
    for item in duplicate:
        print(item)
def Findduplicate():
    records = [
        [1, "Alex", 21],
        [2, "John", 22],
        [1, "Alex", 21],
        [3, "Sam", 23],
        [2, "John", 22]
    ]

    seen = set()

    duplicate = []

    for item in records:
        if tuple(item) in seen:
            duplicate.append(item)
        else:
            seen.add(tuple(item))

    print('Duplicates are :')
    for item in duplicate:
        print(item)

def DuplicateInData():
    file_path = GetDataFile()

    seen = set()
    unique_counter = 0
    duplicat_counter = 0

    with open(file_path,'r',newline='',encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        for item in reader:
            # current = item[fieldnames[0]]
            current = (
                item['InvoiceNo'],
                item['StockCode'],
                item['Quantity'],
                item['UnitPrice']
            )
            if current in seen:
                duplicat_counter += 1
            else:
                seen.add(current)
                unique_counter += 1

        print(f'Total Unique Values : {unique_counter}')
        print(f'Total duplicate Values : {duplicat_counter}')
DuplicateInData()