with open(f'test.bin','rb') as file:
    read = file.read()

print(read)

kbs = 0
with open(f'squertal.jpg','rb') as file:
    # image = file.read()
    while chunk := file.read(1024):
        kbs += 1

print(f'Total kbs of the squertal image : {kbs}')
# with open(f'squert_copy.jpg','wb') as file:
#     file.write(image)