d={}
sentence=input("Enter sentence: ")
#sentence.split()   string ek immutable hota ha so variable assign kr
words=sentence.split()
#print(words)
for i in words:
    #reverse_word=i.reverse()    use reverse() method only for list & not for string
    reverse_word=i[::-1]
    #print(reverse_word)
    d[len(reverse_word)]=tuple(reverse_word)
print(d)
