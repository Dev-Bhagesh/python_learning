import csv

minWeight = 0
maxWeight = 0
totalRecords = 0
avgWeight = 0
first = True
with open('pokemon.csv','r',newline='',encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    sumofweights = 0
    for pokemon in reader:
        totalRecords += 1
        weight = int(pokemon['pokemon_weight'])
        maxWeight = max(maxWeight,weight)
        if first == True:
            minWeight = weight
            first = False

        minWeight = min(minWeight,weight)
        sumofweights += weight

    avgWeight = sumofweights/totalRecords


with open('pokemon_report.txt','w') as file:
    file.write(f'The Total Records of Pokemon : {totalRecords}\n')
    file.write(f'The Maximum Weight of Pokemon in Records : {maxWeight}\n')
    file.write(f'The Minimum Weight of Pokemon in Records : {minWeight}\n')
    file.write(F'The Avarage Weight of Pokemon in Records : {avgWeight}\n')
