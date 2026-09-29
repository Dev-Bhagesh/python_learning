# 1. create a countdown generator
# def CountDown(num,lim):
#     value = num
#     while(value != lim+1):
#         yield value
#         value += 1

# count = CountDown(1,5)
# for i in count:
#     print(i)

# 2. Even numbers generator
def EvenNumbers(num , lim):
    value = num 
    while(value <= lim):
        if value % 2 == 0:
            yield value
        value += 1

even = EvenNumbers(1,10)
for i in even:
    print(i)