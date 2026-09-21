
def manage_students():
    d={}
tup=()
for i in range(1,4):
    name=input("Name: ")
    roll=int(input("Roll No.: "))
    section=input("section: ")
    tup=(roll,section)
    marks=[int(input("sub 1 marks: ")),int(input("sub 2 marks: ")),int(input("sub 3 marks: "))]
#tup=tuple(roll,section)    tumne yahan 2 alag-2 variables daal diye jbki tuple accept only 1 arguments
#tup=(roll,section)    overwrite problem created bcz using of assignment operator
    sum=0
    d[roll]={
       "Students Name":name,
       "Roll & Sections":tup,
       "Marks list":marks,
       "Total Marks":sum()
   }
for Roll_no,Record in d.items():
    print("f Roll_no {Roll_no}:{recprd}")
manage_students()
