# def square():
#     for i in range(0,10):
#         # if i % 2 == 0:
#             # yield i
#         value = i * i
#         if value % 2 == 0:
#             yield value

# gen = square()
# # print(next(gen))

# for i in square():
#     print(i)

# generator comperehece
square = (x * x for x in range(1,11))
print(next(square))
print(next(square))
print(next(square))

for i in square:
    print(i)

even = (x for x in range(0,11) if x % 2 == 0)
for i in even:
    print(i)