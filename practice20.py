


tup=tuple()
for i in range(1,4):
    names=input("Name: ")
    roll=int(input("Roll No.: "))
    section=input("section: ")
    marks=[int(input("sub 1 marks: ")),int(input("sub 2 marks: ")),int(input("sub 3 marks: "))]
    tup=tuple(roll,section)
print(tup)
