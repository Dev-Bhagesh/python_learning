
class Character():
    pass

def choice(choice):
    pass

def SecondLayer(profile):
    name = profile['name']
    age = profile['age']
    role = profile['role']
    inventory = profile['inventory']
    print('-'*25,f' Welcom {name} ','-'*25)

    print(f'Your ID : {profile['id']}')
    print(f'Your Name : {profile['name']}')
    print(f'Your Character : A {profile['role']}')

    print(f'-------- Current Inventory Items --------')

    if inventory:
        for index, item in enumerate(inventory, start=1):
            print(f"\nItem #{index}")
            if 'weapon' in item:
                for weapon in item['weapon']:
                    weapon_name = next(iter(weapon.values()))
                    print(f"  Weapon   : {weapon_name}")
                    print(f"  Damage   : {weapon['damage']}")

            if 'potions' in item:
                for potion in item['potions']:
                    print(f"\n  Potion   : {potion.get('healing', potion.get('poison'))}")
                    print(f"  Effect   : {potion.get('health', potion.get('damage'))}")
                    print(f"  Quantity : {potion['quantity']}")
    else:
        print("  Your inventory is empty!")
        
    while 1 :

        choice = int(input('Currently all services are down so please press 3 to exit : '))
        if choice == 3:
            break