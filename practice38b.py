a=int(input())
b=int(input())
def chocolate(n,m):
    if n%m==0:
        return 0
    else:
        return m-(n%m)
b=chocolate(a,b)
print(b)