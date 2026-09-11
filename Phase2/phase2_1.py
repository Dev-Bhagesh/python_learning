# def chage_number(x,number):
#     numbers = number.copy()
#     x = 20
#     numbers.append(4)
#     print(x,numbers)

# number = [1,2,3]
# x = 10
# print(x)
# print(number)
# chage_number(x,number)
# print(number)
# print(x)

a = [1,2,3]
b = a
c = a.copy()
print(id(a))
print(id(b))
print(id(c))
b.append(4)
c.append(5)
print(a)
print(b)
print(c)