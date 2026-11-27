n=int(input())
#def perfact_no(n):
sum=0
for i in range(1,n):
    if n%i==0:
            sum +=i
if sum==n:
    print("Perfact Number")
else:
    print("Not a Perfact Number")
#b=perfact_no(s)
#print(b)