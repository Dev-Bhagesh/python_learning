def calculate_total(*args):
    total = 0
    for i in args:
        total += i
    print(f'{total}')

# calculate_total(5, 10, 15, 20, 25)

def Show_character(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} : {value}')

Show_character(name="Shadow",
    level=20,
    health=150,
    weapon="Katana")