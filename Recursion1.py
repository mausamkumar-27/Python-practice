s=input()
def reverse(n):
    if n[0]!=n[-1]:
        return False
    else:
        p=n[1:-1]
    return reverse(p)
b=reverse(s)
print(b)