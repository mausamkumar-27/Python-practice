'''def fun(n):
    if n<1:
        return 
    else:
        print(n,end=" ")
        fun(n-1)
fun(5)
print()'''
def asc(n):
    if n<1:
        return
    asc(n-1)
    print(n,end=" ")
asc(5)
print()

