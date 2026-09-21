s=input()
c=len(s)
l=['a','e','i','o','u','A','E','I','O','U']
for i in range(c):
    if s[i] in l:
        print(s[i],i)