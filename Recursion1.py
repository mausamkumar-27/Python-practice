'''s=input()
def reverse(n):
    if len(n)<=1:
        return True
    else:
        if n[0]!=n[-1]:
            return False
        else:
            p=n[1:-1]
    return reverse(p)
b=reverse(s)
print(b)'''