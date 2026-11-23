from datetime import datetime
import json

# quantities = ["5", "-5", "0", "abc", "10"]
# for value in quantities:
#     try:
#         val = int(value)
#         print(val)
#     except ValueError as error:
#         print(f'Invalid Value : {value}')
# prices = ["10.50", "25", "-20.5", "abc", "0.00"]
# for value in prices:
#     try:
#         val = float(value)
#         if val > 0:
#             print(f'Valid Price : {val}')
#         elif val <= 0:
#             print(f'Invalid Price : {val}')
#     except ValueError:
#         print(f"Invalid Value : {value}")


# dates = [
#     "12/01/2010 08:26",
#     "12/02/2010 10:45",
#     "invalid date",
#     "25/15/2010 12:30"
# ]

# for date in dates:
#     try:
#         value = datetime.strptime(date, "%m/%d/%Y %H:%M")
#         print(f"The date is : {value}")
#     except ValueError:
#         print(f'Invalid Date : {date}')

records = [
    {"Quantity": "5", "UnitPrice": "10.50"},
    {"Quantity": "abc", "UnitPrice": "20.00"},
    {"Quantity": "-5", "UnitPrice": "15.00"},
    {"Quantity": "10", "UnitPrice": "invalid"},
    {"Quantity": "invalid", "UnitPrice": "invalid"}
]

invalid_records = []
valid_records = []

for value in records:
    qunt = False
    unit = False
    errors = []
    # try:
    #     quantity = int(value['Quantity'])
    #     unitprice = float(value['UnitPrice'])

    #     if type(quantity) == int and type(unitprice) == float :
    #         if unitprice > 0:
    #             valid_records.append(value)
    #         else:
    #             invalid_records.append(value)

    # except ValueError:
    #     print('Invalid Value')
    #     invalid_records.append(value)
    try:
        qunatity = int(value['Quantity'])
        qunt = True
    except ValueError:
        print(f'Invalid Quantity : {value}: {value['Quantity']}')
        # invalid_records.append(value)
        errors.append("Invalid Quantity")

    try:
        unitprice = float(value['UnitPrice'])
        unit = True
    except ValueError:
        print(f'Invalid UnitPrice :{value} : {value['UnitPrice']}')
        # invalid_records.append(value)
        errors.append("Invalid UnitPrice")

    if unitprice <= 0:
        errors.append('Non-Positive Unit Price')

    if len(errors) > 0:
        record = {
            "Original Record" : value,
            "Errors" : errors
        }
        
        invalid_records.append(record)
    else:
        valid_records.append(value)

print(f"Valid Records : {json.dumps(valid_records)}")
print(f'Invalid Records : {json.dumps(invalid_records)}')