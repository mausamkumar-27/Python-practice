sentence="Python programming is very powerful and easy"
words=sentence.split()
#print(words)
'''lists=[len(w) for w in words]
#print(lists)
print(list(zip(words,lists)))'''

length_list=[]
for i in words:
    length_list.append(len(i))
print(list(zip(words,length_list)))