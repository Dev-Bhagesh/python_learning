import expence_calculator

def Add():
    exp = input("Enter the expense name : ")
    amount = input("Enter the amount :")
    id = 0
    with open("Expense.txt",'r') as file:
        if file != "":
            for i in file:
                if i != '\n':
                    value = i
                    value2 = value.split(':')
                    value3 = value2[0].strip()
                    value4 = int(value3)
                    id = value4 + 1

    with open("Expense.txt",'a') as file:
        file.write('\n')
        file.write(f'{id} : ')
        file.write(f'{exp} => ')
        file.write(f'{amount}') 
        file.write('\n')

    return 1

def View():
    with open('Expense.txt','r') as file:
        data = file.read()
        print(data)
        return 2

def CalculateExpenses():
    choice = int(input("1.Total Expence \n2.Catrgorycal Expense \nEnter the choice: "))
    data = []
    match choice:
        case 1 :
            with open('Expense.txt','r') as file:
                for i in file:
                    value = i
                    value2 = value.split('=>')
                    if i != "\n" :
                        value3 = int(value2[1].strip())
                        data.append(value3)

                total = expence_calculator.TotalSum(data)
                print(total)                                     

        case _ : return print("Selected Status is Not correct")

def SearchExpense():
    inp = input("Search the Expense: ")
    with open('Expense.txt','r') as file:
        for i in file:
            value = i
            if value != "\n":
                temp = value.split('=>')
                temp2 = temp[0].split(':')
                value2 = temp2[1].strip()
                if i != "\n":
                    if value2 == inp:
                        print(f'{i}')

def DeleteExpense():
    lines = []
    choice = int(input("1:Delete One Expense \n2: Delete All \nEnter the Choice: "))
    if choice == 2:
        with open('Expense.txt','w') as file:
            file.write("")
    elif choice == 1:
        with open('Expense.txt','r') as file:
            for i in file:
                print(i)

        inp = int(input("Enter the id of the Expense: "))
        with open('Expense.txt','r') as file:
            for i in file:
                if i != '\n':
                    value = i
                    # print(f'Value -> {value}')
                    value2 = value.split(':')
                    # print(f"Value2 -> {value2}")
                    value3 = int(value2[0].strip())
                    # print(f'Value3 -> {value3}')
                    if value3 != inp:
                        st = str(i)
                        # print(f'**** st is updated ->{st}')
                        lines.append(st)
                        # print(f'lines.append() run ****')
                # print("-----------------------------------------")

        print(lines)
        with open('Expense.txt','w') as file:
            file.writelines(lines)
            
    else:
        print("Not correct selection")