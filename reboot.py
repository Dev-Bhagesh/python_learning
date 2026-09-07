a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = a+b
print(c)

age = int(input("Enter the age of the person"))
if age>18 and age<60:
    print("The person is a adult")
elif (age>60):
    print("The person is old")
else:
    print("The person is a child")

for i in range(100):
    if(i%2 == 0):
        print(i)

lang = ['JavaScript',"C++","TypeScript","Python","Java"]
for i in range(len(lang)):
    print(lang[i])

def Larg(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

print(Larg(5,10,4))

name = input("Enter the Name : ")
print(f"My name is {name}")
print(name)
print(name.upper())
print(name.lower())
print(len(name))
print(name.split(" "))
print(name.strip())
print(name[::-1])
print(name[:7])

pc = {
    "os" : "windows 10",
    "cpu":"amd ryzen 5600g",
    'ram':'8gb',
    'ssd':'512gb',
    'python version':'v3.14',
}

for key , value in pc.items():
    print(f" {key} -> {value}")

folder_a = {'a.pdf','b.jpg','a,jpg','a.pdf','c.doc'}
folder_b = {'a.doc','b.pdf','a.pdf','b.jpg','e.json'}

folder_c = folder_a.union(folder_b)
print(folder_c)
folder_c = folder_a.intersection(folder_b)
print(folder_c)
folder_c = folder_a.difference(folder_b)
print(folder_c)
folder_c = folder_b.difference(folder_a)
print(folder_c)