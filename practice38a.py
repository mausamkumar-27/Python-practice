s=input()
def reverseString(n):
    if n[::-1]==n:
        return True
    else:
        return False
b=reverseString(s)
print(b)