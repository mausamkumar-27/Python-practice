n=int(input())
w=[int(i) for i in input().split()]
m=int(input())
def adjusted_weight(weights,modifier,index):
    if index==len(weights):
        return 0
    
    return weights[index]+adjusted_weight(weights,modifier,index+1)
    
    if modifier>0:
        return total-modifier
    elif modifier<0:
        return total+modifier
    else:
        return total
b=adjusted_weight(w,m,0)
print(b)