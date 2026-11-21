'''from functools import reduce 
n=int(input())
l=[int(i) for i in range(1,n+1)]
a=reduce(lambda x,y:x+y,l)
print("Total Sum:",a)'''
'''n=int(input())
def total_sum(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return n+total_sum(n-1)
print("Total Sum:",total_sum(n))'''
def no(n):
    if n<1:
        return
    print(n,end=" ")
    no(n-1)
print(no(-5))