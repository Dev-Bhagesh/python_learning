
with open('pokemon.txt','r') as file:
    print('starting position:',file.tell())
    data = file.read(7)
    print(f'Data : {data}')
    print(f'Current position : {file.tell()}')
    data = file.read(9)
    print(f'Current data : {data}')
    print(f'Current Position : {file.tell()}')
    file.seek(0)
    data = file.read(7)
    print(f'Current data :{data}')
    print(f'current position : {file.tell()}')
    