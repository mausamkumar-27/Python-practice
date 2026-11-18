#from functools import reduce
raw_records = [
    "  rahul kumar , computer science , 85 , 12  ",
    "Priya Sharma, Electronics, 92, 15",
    "  amit singh , mechanical , 45 , 6 ",
    "sneha gupta, Computer Science, 78, 10",
    "  vikas verma , civil , 35 , 4 "
]
zip_list=["name","course","marks","hours"]
cleaned_records=list(map(lambda x:x.strip().split(","),raw_records))
#print(cleaned_records)
zip_cleaned=list(map(lambda y:list(zip(zip_list,y)),cleaned_records))
#print(zip_cleaned)
my_dict=list(map(lambda y:dict(y),zip_cleaned))
#print(my_dict)
updated_dict=list(map(lambda x:{
    **x,
    "name":x["name"].title(),"course":x["course"].lower(),"marks":int(x["marks"]),"hours":int(x["hours"])
},my_dict))
#print(updated_dict)
class student:
    def __init__(self,name,course,marks,hours):
        self.name=name
        self.course=course
        self.marks=marks
        self.hours=hours
    def is_passed(self):
        if self.marks>=50:
            return True
        else:
            return False
student_object=[student(**item) for item in updated_dict]
#for s in student_object:
    #print(f"Name:{s.name} , Course:{s.course} , Marks:{s.marks} , Hours:{s.hours} , Passed:{s.is_passed()}")
'''filtered_data=list(filter(lambda x:x.is_passed(),student_object))
for p in filtered_data:
    print(f"Name:{p.name} , Course:{p.course} , Marks:{p.marks} , Hours:{p.hours} , Passed:{p.is_passed()}")'''
check=list(map(lambda y:student(**y),updated_dict))
print(check)