# normal functions
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

# *args call
def args(*args):
    sum = 0
    for i in args:
        sum = sum+i
    return sum

def argsCall():
    print(args(2,3,4,5))

# **kwargs example
def kwArgs(**bhagesh):
    for key,value in bhagesh.items():
        print(f'{key} : {value}')

def kwArgsCall():
    kwArgs(name = 'Bhagesh',age=21,role='developer')

#combination of both *args and **kwargs in one function
def combineBoth(*args,**kwargs):
    for i in args:
        print(f'{i} \n')

    for key,value in kwargs.items():
        print(f'{key} : {value}')

def combineBothCall():
    combineBoth('Bhagesh',21,'Developer',country = 'India',active=True)

#normal function
def Squar(num):
    return num*num

#lambda function Example
def lambdaExample():
    cube = lambda cub: cub*cub*cub
    print(cube(4))

    isEven = lambda num:True if num % 2 == 0 else False
    print(isEven(11))

#assigning functions for variables  
def mult(a,b):
    return a*b

def multCall():
    mul = mult
    print(mul(5,10))

# passing functions as arguments to another function
def multiply(a,b):
    return a*b

def outerFunction(operation,a,b):
    return operation(a,b)

def OuterFunctionCall():
    result = outerFunction(multiply,5,5)
    print(result)

#returning a function
def Outer():
    def inner():
        return print("hello")
    return inner()

def OuterCall():
    out = Outer
    print(out())

#example function
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def calculator(operation):
    if(operation == "add"):
        return add
    else:
        return subtract

def calculatorCall():
    cal = calculator('add')
    print(cal(5,2))
    cal = calculator('subtract')
    print(cal(5,2))

def main():
    calculatorCall()

main()