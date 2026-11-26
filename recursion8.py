n=int(input())
w=[int(i) for i in input().split()]
m=int(input())
def sum_weight(weights,index):
    if index==len(weights):
        return 0
    return weights[index]+adjusted_weight(weights,index+1)
def adjusted_weight(weights,modifier,index):
    total=sum_weight(weights,index)
    if modifier>0:
        return total-modifier
    elif modifier<0:
        return total+modifier
    else:
        return total
b=adjusted_weight(w,m,0)
print(b)