
# with open('utfile.txt','w',encoding='utf-8') as file:
#     file.write('''Pikachu
# ピカチュウ
# Charizard 🔥
# नमस्ते''')

pokemon = 'Charizard 🔥'
print(pokemon)
pokemon = pokemon.encode("utf-8")
print(pokemon)
print(type(pokemon))
pokemon = pokemon.decode('utf-8')
# pokemon = b"Charizard 🔥"
print(pokemon)