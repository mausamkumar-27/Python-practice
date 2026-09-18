
sentence=input("Enter sentence: ")
#sentence.split()   string ek immutable hota ha so variable assign kr
words=sentence.split()
#print(words)
for i in words:
    reverse_word=i.reverse()
    print(reverse_word)