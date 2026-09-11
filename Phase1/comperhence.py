# nums = [2,4,6,8,10]
# squrs = [n * n for n in nums]
# print(squrs)

# nums2 = list(i for i in range(1,51) if i % 2 == 0)
# print(nums2)

# files = ["hello.py","a.jpg","b.doc","c.py","j.py"]
# files2 = [i for i in files if i.endswith('.py')]
# print(files2)

# nums = [1,2,3,4,5,6]
# cubes = {n:n ** 3 for n in nums}
# print(cubes)

# scors = {"Alice":85,"Bob":42,"Charlie":91,"Devid":55,"Eve":73}
# ranks = {n:i for n,i in scors.items() if i>=60}
# print(ranks)

setFiles = {'app.py','hi.jpg','no.cpp','by.py','app.py','hi.jpg'}
setfiles2 = {i.split('.')[-1] for i in setFiles}
print(setfiles2)