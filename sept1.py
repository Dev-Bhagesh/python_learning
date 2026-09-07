# #3 problem
# str1 = input("Enter a string: ");
# str = str1.split()
# # n = 256;
# hash = [0] * 256;

# for i in str1:
#     # cha = str[i]
#     asc = ord(i)
#     hash[asc] += 1

# for i in range(256):
#     if hash[i] != 0:
#         alp = chr(i)
#         print(f'{alp} => {hash[i]}') 

#4 problem
List = list(input("Enter the List: "))
print(List)
# temp = List
indexes = []
for i in range (len(List)):
    # index = i+1
    for j in range(i+1,len(List)):
        if List[i] == List[j]:
            indexes.append(j)


for i in range(len(indexes)-1,-1,-1):
    List.pop(indexes[i])

print(List)