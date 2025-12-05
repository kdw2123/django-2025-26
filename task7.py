sent = input("enter the sentence you want  : ")
words = sent.split()
dict = {}
for word in words :
    word = word.lower()
    if word in dict:
      dict[word] += 1
    else:
     dict[word] = 1
print("word frquency",dict)
