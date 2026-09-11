with open("note.txt",'w') as file:
    file.write("hello world")

with open('note.txt','r') as file:
    data = file.read()
    with open('note.txt','a') as files:
        files.write(" I Love you sakshi")
    file.seek(0)
    refresh = file.read()

print(data)
print(refresh)