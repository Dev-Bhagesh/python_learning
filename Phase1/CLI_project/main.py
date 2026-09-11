exit = True
import oper

def default():
    print("Selection Not allowed")


def mainMenu(choice):
    global exit
    match choice:
        case 1: oper.Add()
        case 2: oper.View()
        case 3: oper.CalculateExpenses()
        case 4: oper.SearchExpense()
        case 5: oper.DeleteExpense()
        case 7: return 0
        case _: return print("Selection not allowed")

while(exit):
    print('================================================================')
    print("Welcome to Expence Tracker")
    print("1 : Add Expense \n2 : View Expenses \n3 : Calculate All Expenses \n4 : Search Expense " \
    "\n5 : Delete Expenses \n7: Exit")

    choice = int(input("Select the Choice: "))

    status = mainMenu(choice)
    if status == 0:
        exit = False
