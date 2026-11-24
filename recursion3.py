n=int(input())
def count_ways(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return count_ways(n-1)+count_ways(n-2)
b=count_ways(n)
print(b)