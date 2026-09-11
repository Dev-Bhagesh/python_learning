# numbers = [1,2,2,3,4,5,5,6,4,7,8]
# nums = set(numbers)
# print(nums)

# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# C = A & B
# D = A.union(B)
# E = A-B
# F = B-A
# G = A ^ B
# print(C ,D, E, F)
# print(G)

# number2 = {10,20,30,40}
# number2.add(50)
# number2.add(60)
# number2.remove(20)
# number2.discard(100)
# print(number2)

# students = {"Rahul", "Aman", "Bhagesh", "Ravi", "Kiran"}
# value = 'Sakshi' not in students
# print(value)

#create a list without duplicates
# L1 = [1,2,3,3,4,2,5,6,4]
# S1 = set(L1)
# L2 = list(S1)
# print(L2)

# python = {"Aman", "Rahul", "Bhagesh", "Ravi"}
# cpp = {"Bhagesh", "Ravi", "Kiran", "Arjun"}
# KnowBoth = python.intersection(cpp) #python & cpp
# print(KnowBoth)
# knowPythonOnly = python - cpp 
# print(knowPythonOnly)
# KnowOneOfTwo = python ^ cpp
# print(KnowOneOfTwo)

numbers = [10, 20, 30, 40, 50]

total = 0

for i in range(len(numbers)):
    total = total + numbers[i + 1]

average = total / len(numbers)

print("Total:", total)
print("Average:", average)