class InvalidOperatorError(Exception):
    pass

try:
    num1 = int(input("Enter the number 1 : "))
    oper = input("Enter the Operator (+ / * -): ")
    num2 = int(input("Enter the number 2 : "))

    if oper not in ['+','-','*','/']:
        raise InvalidOperatorError("Invalid Operator")

    if(oper == '+'):
        result = num1 + num2;
        print(f"The answer is {result}")
    elif(oper == "-"):
        result = num1 - num2;
        print(f"The answer is {result}")
    elif(oper == "*"):
        result = num1 * num2;
        print(f"The answer is {result}")
    else:
        result = num1 / num2;
        print(f"The answer is {result}")

except InvalidOperatorError as e:
    print(e)

except ValueError:
    print("Invalid Number")

except ZeroDivisionError:
    print("Zero is not allowed")