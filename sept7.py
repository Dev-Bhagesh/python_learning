# st = input("Enter a list of numbers: ")
# L1 = [int(x) for x in st.split(',')]
# print(L1)
# hash = [0] * 257
# for i in L1:
#     hash[i] += 1

# L2 = []
# for i in L1:
#     if hash[i] == 1:
#         L2.append(i)

# print(L2)

# st2 = input("Enter the list: ")
# L1 = [int(x) for x in st2.split(',')]
# print(L1)
# rangE = len(L1)
# neg = 0
# indexes = []
# print(f'length of L1 : {rangE}')
# count = 0;
# for i in range(0,rangE-1):
#     if L1[i] == 0:
#         indexes.append(i)
#         count += 1

# print(f'counts of 0 :{count}')
# print(f'Indexes : {indexes}')
# for i in range(0,len(indexes)):
#     L1.pop(indexes[i]-neg)
#     neg += 1

# for i in range(1,count+1):
#     L1.append(0)

# print(L1)

st3 = input("Enter the list : ")
L1 = [int(x) for x in st3.split(',')]
max = 0
secM = 0
# nex = L1[1]

for i in L1:
    if max < i:
        max = i

for i in L1:
    if i < max and i > secM :
        secM = i

print(f'Second largest element of the list : {secM}')
