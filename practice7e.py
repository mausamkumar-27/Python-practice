marks_list=[95,82,67,45,89,32,74]
for mark in marks_list:
    if(mark>=90):
        print("Grade A+")
    elif(mark>=80 and mark<90):
        print("Grade A")
    elif(mark>=60 and mark<80):
        print("Grade B")
    elif(mark>=40 and mark<60):
        print("Grade C")
    else:
        print("Failed")
    