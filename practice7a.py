records=(("Mausam",85),("Harry",92),("Ali",78))
student_dict={}
for name,marks in records:
    student_dict[name]=marks            
print(student_dict)
print(student_dict.get("Ali"))
print(student_dict.get("Rohan"))
