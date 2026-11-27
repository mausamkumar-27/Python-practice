def square(a):
    return a**2
def rectangle(a,b):
    return a*b
def triangle(a,b):
    return a*b*0.5
s=float(input())
len,bre=map(float,input().split())
base,h=map(float,input().split())
p=square(s)
q=rectangle(len,bre)
r=triangle(base,h)
print(f"{p:.2000f}")
print(f"{q:.2000f}")
print(f"{r:.2000f}")