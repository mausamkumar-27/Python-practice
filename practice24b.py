sentence="Python programming is very powerful and easy"
words=sentence.split()
#print(words)
lists=[len(w) for w in words]
#print(lists)
print(list(zip(words,lists)))