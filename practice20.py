

d={}
tup=()
for i in range(1,4):
    names=input("Name: ")
    roll=int(input("Roll No.: "))
    section=input("section: ")
    marks=[int(input("sub 1 marks: ")),int(input("sub 2 marks: ")),int(input("sub 3 marks: "))]
#tup=tuple(roll,section)    tumne yahan 2 alag-2 variables daal diye jbki tuple accept only 1 arguments
#tup=(roll,section)    overwrite problem created bcz using of assignment operator
    d['n']=d.get('n',())+tup
print(tup)
