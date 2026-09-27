nums=[3,6,9]
new_nums=list(map(lambda x:x/2,nums))
print(new_nums)


words=["apple","bat","cat","elephant"]
new_words=list(filter(lambda x:len(x)>3,words))
print(new_words)

from functools import reduce
numbers=[5,4,3,2]
new_numbers=reduce(lambda x,y:x-y,numbers)
print(new_numbers)

scores=[45,80,33,90,60,50,12,54]
scores1=list(filter(lambda x: x>=50,scores))
scores2=list(map(lambda x: x+5,scores1))
print(scores2)

x=[10,20,30]
y=x
z=[10,20,30]
print(x==z)
print(x is z)
print(x is y)