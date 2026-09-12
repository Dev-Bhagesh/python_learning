def User(name,age,country = 'India',isAdmin = False):
    if (name and age):
        print(f"User {name} age {age} country {country}")
        if(isAdmin):
            print(f"This user is admin")
    return 'Success'

def UserCall():
    name = 'Bhagesh'
    age = 21
    country = 'India'
    isAdmin = True
    print(User(name,age,isAdmin=isAdmin))


def args(*args):
    sum = 0
    for i in args:
        sum = sum+i
    return sum

def argsCall():
    print(args(2,3,4,5))

def kwArgs(**bhagesh):
    for key,value in bhagesh.items():
        print(f'{key} : {value}')

def kwArgsCall():
    kwArgs(name = 'Bhagesh',age=21,role='developer')

def combineBoth(*args,**kwargs):
    for i in args:
        print(f'{i} \n')

    for key,value in kwargs.items():
        print(f'{key} : {value}')

def combineBothCall():
    combineBoth('Bhagesh',21,'Developer',country = 'India',active=True)

def Squar(num):
    return num*num

def main():
    # print(Squar(5))
    cube = lambda cub: cub*cub*cub
    print(cube(4))

    isEven = lambda num:True if num % 2 == 0 else False
    print(isEven(11))

main()