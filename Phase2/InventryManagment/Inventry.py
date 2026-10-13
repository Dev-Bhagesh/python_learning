import json
from pathlib import Path

class Item():
    def __init__(self,item):
        return item

class Inventry():

    CHAR_DIR = Path(__file__).parent/f'Characters'

    def __init__(self,profile):
        self.name = profile['name']
        self.id = profile['id']
        self.age = profile['age']
        self.role = profile['role']
        self.current_inventory = profile['inventory']
        self.file_path = Inventry.CHAR_DIR/f'characters.json'
        
    
class Weapon(Inventry):
    def __init__(self,profile):
        super().__init__(profile)
        if self.role == "Swards Man":
            self.wepons_list = {
                1:{
                    'name':'Dragon Sword',
                    'discription' : "A  legendary, mythic blade—frequently forged from a dragon's fang, scale, or ancient metal—imbued with draconic magic, elemental power, or fiery energy.",
                    'damage':30,
                },
                2:{
                    'name':'Golden Sword',
                    'discription' : "A  radiant, high-status weapon featuring a blade, hilt, or full mountings crafted from or plated in gold ",
                    'damage':25,
                }
            }
        elif self.role == 'Archer':
            self.wepons_list = {
                1:{
                    'name':'Ice Arrow',
                    'discription' : "A  magical or specialized projectile that freezes targets, deals cold damage, or creates ice platforms upon impact.",
                    'damage': 15
                },
                2:{
                    'name':'Poison Arrow',
                    'discription' : " an arrow or dart treated with a toxic substance—derived from plants, animals, or minerals—used historically and across indigenous cultures for hunting and warfare.",
                    'damage': 30
                },
                3:{
                    'name':'Powr Bow',
                    'discription' : "A stores more mechanical energy to launch an arrow faster, flatter, and with greater impact. ",
                    'damage': 25
                }
            }
        elif self.role == 'Knight':
            self.wepons_list = {
                1:{
                    'name' : 'Lance',
                    'discription' : "A  long, heavy pole weapon featuring a sharp metal point.",
                    'damage':30,
                },
                2:{
                    'name' : 'Battle Axe',
                    'discription' : " A  specialized, long- or short-handled weapon with a heavy metal blade designed specifically for close-range combat, piercing armor, and splitting shields. ",
                    'damage' : 35
                }
            }
        elif self.role == 'Wizard':
            self.wepons_list = {
                1:{
                    'name' : 'Arcane Grimoire',
                    'discription' : " A specialized magic item designed to boost the save DC and attack rolls of a wizard's spells.",
                    'damage' : '20'
                },
                2:{
                    'name' : 'Spellbook',
                    'discription' : "Read or held to project arcane symbols and cast ranged magic. ",
                    'damage' : 20
                },
                3:{
                    'name' : 'Wand',
                    'discription' : "Light, quick, and traditional for directing focused bursts of magic. ",
                    'damage' : 25
                },
                4:{
                    'name' : 'Orb',
                    'discription' : " Held or levitated to project arcane energy, boost spell damage, or disarm opponents. ",
                    'damage' : 30
                }
            }
        else:
            print('You are not Eligible for weapon')

    def AddItemToInv(self):
        print(f'*'*10 + ' Chose The Wepon You Want '+'*'*10)
        for key,value in self.wepons_list.items():
            print(f'{key}:Name       : {self.wepons_list[key]['name']}')
            print(f'     Damae       : {self.wepons_list[key]['damage']}')
            print(f'     Discription : {self.wepons_list[key]['discription']}')
            print('\n')
            print('-'*25)

        choice = int(input('Enter the Choice : '))

        weapon_selected = self.wepons_list[choice]
        Weapons = self.current_inventory[0]['Weapons']

        if any(weapon_selected['name'] == isweapon['name'] for isweapon in Weapons):
            print('Weapon alredy exists in inventry')
        else:
            with open(f'{self.file_path}','r') as file:
                ReadFile = json.load(file)
            

            ReadProfile = next(profile for profile in ReadFile if profile['id'] == self.id)
            ReadProfile['inventory'][0]['Weapons'].append(self.wepons_list[choice])

            # ReadFile[self.id] = ReadProfile

            with open(f'{self.file_path}','w') as file :
                json.dump(ReadFile,file,indent=4)



    def RemoveItems(self):
        print(f'*'*10 + ' Chose the Wepon To Remove '+'*'*10)
        current_wepons_list = self.current_inventory[0]['Weapons']

        num = 1
        for weapon in current_wepons_list:
            print(f'{num} Name       : {weapon['name']}')
            print(f'  Damage     : {weapon['damage']}')
            print(f'  Discription: {weapon['discription']}')
            print('-'*10)
            num += 1

        # for currentWeapon in current_wepons_list:
        #     for key in currentWeapon:
        #         print(f'{key} Name       : {currentWeapon['name']}')
        #         print(f'Damage     : {currentWeapon['damage']}')
        #         print(f'Discription: {currentWeapon['discription']}')
        #         print('-'*10)

        choice = int(input('Enter the Choice : '))
        weapon_selected = current_wepons_list[choice-1]

        with open(f'{self.file_path}','r') as file:
            ReadFile = json.load(file)

        ReadProfile = ReadFile
        ReadProfile = next(profile for profile in ReadFile if profile['id'] == self.id)
        ReadProfile['inventory'][0]['Weapons'].remove(weapon_selected)
        
        with open(f'{self.file_path}','w') as file:
            json.dump(ReadFile,file,indent=4)




class Potion(Inventry):
    def __init__(self, profile):
        super().__init__(profile)
        self.postions_list = {

            1:{
                'name' : 'Healing Potion',
                'discription' : 'Heals 30 HP of the character .',
                'health' : 30,
            },
            2:{
                'name' : 'Antidote',
                'discription' : 'Remove any status condition on character .',
                'health' : 0
            },
            3:{
                'name' : 'Rage Potion',
                'discription' : 'Rages the Character and increase the attack damage slightly .',
                'health' : 2
            }
        }

    def AddItemToInv(self):
        print(f'*'*10+' Chose The Potion You Want '+'*'*10)
        for key,value in self.postions_list.items():
            print(f'Name        : {self.postions_list[key]['name']}')
            print(f'Health      : {self.postions_list[key]['health']}')
            print(f'Discription : {self.postions_list[key]['discription']}')
            print('\n')
            print('-'*25)

        choice = int(input('Enter the Choice : '))

        potion_selected = self.postions_list[choice]
        potions = self.current_inventory[1]['Potions']

        if any(potion_selected['name'] == ispotion['name'] for ispotion in potions):
            print('Potion alredy exists in inventry')
        else:
            with open(f'{self.file_path}','r') as file:
                ReadFile = json.load(file)

            ReadProfile = next(profile for profile in ReadFile if profile['id'] == self.id)
            ReadProfile['inventory'][1]['Potions'].append(self.postions_list[choice])

            with open(f'{self.file_path}','w')as file:
                json.dump(ReadFile,file,indent = 4)

    def RemoveItem(self):
        print(f'*'*10 + ' Chose the Potion You Want to Remove '+'*'*10)
        current_potion_list = self.current_inventory[1]
        for key , value in current_potion_list:
            print(f'{key}. Name      : {current_potion_list[key]['name']}')
            print(f'       Health     : {current_potion_list[key]['health']}')
            print(f'       Discription: {current_potion_list[key]['discription']}')

        choice = int(input('Enter the Choice : '))
        potion_selected = current_potion_list[choice]

        with open(f'{self.file_path}','r') as file:
            ReadFile = json.load(file)

        ReadProfile = ReadFile
        ReadProfile[self.id]['inventory']['Potions'].remove(potion_selected)

        with open(f'{self.file_path}','w') as file:
            json.dump(ReadFile,file,indent=4)


def AddingItems(profile):
    name = profile['name']
    age = profile['age']
    role = profile['role']
    current_inventry = profile['inventory']

    # Inv = Inventry(profile)

    inv_type = {
        1:'Weapons',
        2:'Potions'
    }

    print('\n')
    print(f'-'*25)
    print('\n')

    for key,value in inv_type.items():
        print(f'{key} : {value}')
    
    choice = int(input('Enter the Choice : '))

    if choice == 1:
        weapon = Weapon(profile)
        weapon.AddItemToInv()
    else:
        potion = Potion(profile)
        potion.AddItemToInv()

def RemovingItems(profile):
    inv_type = {
        1:'Weapons',
        2:'Potions'
    }

    print('\n')

    for key,value in inv_type.items():
        print(f'{key} : {value}')

    choice = int(input('Enter the choice : '))

    if choice == 1:
        weapon = Weapon(profile)
        weapon.RemoveItems()
    else:
        potion = Potion(profile)
        potion.RemoveItem()