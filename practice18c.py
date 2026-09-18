d={}
sentence=input("Enter sentence: ")
#sentence.split()   string ek immutable hota ha so variable assign kr
words=sentence.split()
#print(words)
for i in words:
    #reverse_word=i.reverse()    use reverse() method only for list & not for string
    reverse_word=i[::-1]
    #print(reverse_word)
    #d[len(reverse_word)]=tuple(reverse_word)      use comma bcz ye reverse_word ka char as tuple dega 
    #d[len(reverse_word)]=tuple(reverse_word,)     for add multipl item use .get() method othrwse overwrite problem create
    #d[len(reverse_word)]=tuple(d.get(reverse_word))    inside .get() you forgot to give key
    #d[len(reverse_word)]=d.get(len(reverse_word), ())+ reverse_word   only concatenate tuple to tuple  not string to tuple
    d[len(reverse_word)]=d.get(len(reverse_word), ())+ (reverse_word ,)  # trailling comma bhi lga
print(d)
