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
    "name":x["name"].title(),"course":x["course"].strip().lower(),"marks":int(x["marks"]),"hours":int(x["hours"])
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
student_object=list(map(lambda y:student(**y),updated_dict))
#for i in student_object:
    #print(f"{i.name},{i.course},{i.marks},{i.hours},{i.is_passed()}")

filtered_data=list(filter(lambda x:x.is_passed(),student_object))
#print(filtered_data)
#for p in filtered_data:
    #print(f"Name:{p.name} , Course:{p.course} , Marks:{p.marks} , Hours:{p.hours} , Passed:{p.is_passed()}")
passed_name=[i.name for i in filtered_data]
#print(passed_name)
unique_course={j["course"] for j in updated_dict}
print(unique_course)