import subprocess

print('Convert Pokemon_json.json -> Pokemon_csv.csv Press : 1')
print('Convert pokemoncsv.csv -> pokemonjson.json Press : 2')
userIn = int(input('Enter Your Choice:'))

if userIn == 1:
    try:
        result = subprocess.run(
            ['python','converTocsv.py'],
            capture_output=True,
            check=True,
            text=True
        )
        print(result)

    except subprocess.CalledProcessError as error:
        print("Error has occured")

elif userIn == 2:
    try:
        result = subprocess.run(
            ['python','convertTojson.py'],
            capture_output=True,
            text=True,
            check=True
        )

        print(result)
    except subprocess.CalledProcessError as error:
        print('Error has occured')
