import Inventry

class Character():
    pass

def Choice(choice,profile):
    match choice:
        case 1 : Inventry.AddingItems(profile)
        case 2 : Inventry.RemovingItems(profile)
        case _ : print('Invalid choice')

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

    # if inventory:
    #     for index, item in enumerate(inventory, start=1):
    #         print(f"\nItem #{index}")
    #         if 'weapon' in item:
    #             for weapon in item['weapon']:
    #                 weapon_name = next(iter(weapon.values()))
    #                 print(f"  Weapon   : {weapon_name}")
    #                 print(f"  Damage   : {weapon['damage']}")

    #         if 'potions' in item:
    #             for potion in item['potions']:
    #                 print(f"\n  Potion   : {potion.get('healing', potion.get('poison'))}")
    #                 print(f"  Effect   : {potion.get('health', potion.get('damage'))}")
    #                 print(f"  Quantity : {potion['quantity']}")
    if inventory:
        for items in inventory:
            print('-'*25)
            # print(f'{inventory[index][key]}')
            if 'Weapons' in items:
                for weapon in items['Weapons']:
                    weapon_name = next(iter(weapon.values()))
                    print(f' Weapon : {weapon_name}')
                    print(f' Damage : {weapon['damage']}')

        

            if 'Potions' in items :
                for potion in items['Potions']:
                    potion_name = next(iter(potion.values()))
                    print(f' Potion    : {potion_name}')
                    print(f' Attribute : {potion['discription']}')
        print('\n')
    else:
        print("  Your inventory is empty!")

    print('-'*50)
    
    while 1 :
        print(f'-'*25+' Chose Options From Below '+f'-'*25)    
        tasks = {
            1:'Add Item To Inventry',
            2:'Remove Item From Invetry',
            3:'Exit'
        }

        for key,value in tasks.items():
            print(f'{key} : {value}')

        choice = int(input('Enter Your Choice : '))

        if choice < 3 and choice > 0 :
            Choice(choice,profile)
        else:
            break
