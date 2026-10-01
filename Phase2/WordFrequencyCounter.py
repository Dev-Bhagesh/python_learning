sentence = input('Enter the String : ')
sentence = sentence.replace(',',"")
sentence = sentence.replace('.','')
sentence = sentence.replace('/','')
sentence = sentence.replace('!','')
sentence = sentence.lower()
wordArray = sentence.split(' ')

print(wordArray)

dict = {}

for i in wordArray:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)