import csv

pokemon = [
    [25, "Pikachu", "Electric", 4, 6.0],
    [6, "Charizard", "Fire", 78, 90.5],
    [9, "Blastoise", "Water", 79, 85.5],
    [3, "Venusaur", "Grass", 80, 100.0],
    [150, "Mewtwo", "Psychic", 106, 122.0],
    [94, "Gengar", "Ghost", 60, 40.5],
    [143, "Snorlax", "Normal", 110, 460.0],
    [149, "Dragonite", "Dragon", 91, 210.0],
    [130, "Gyarados", "Water", 95, 235.0],
    [448, "Lucario", "Fighting", 70, 54.0]
]

with open('poke.csv','w',encoding='utf-8',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(('ID','Name','Type','Attack','Waight'))
    writer.writerow(pokemon[0])
    writer.writerow(pokemon[1])
    writer.writerow(pokemon[3])

