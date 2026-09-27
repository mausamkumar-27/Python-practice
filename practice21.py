nums=[3,6,9]
new_nums=list(map(lambda x:x/2,nums))
print(new_nums)


words=["apple","bat","cat","elephant"]
new_words=list(filter(lambda x:len(x)>3,words))
print(new_words)