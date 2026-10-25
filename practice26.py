#from functools import reduces
students=["Aman","Priya","Rohan","Divya","Karan"]
attendence_pct=[85,92,78,95,60]
mid_term_scores=[70,88,55,90,45]
end_term_scores=[75,92,60,94,50]
attendence=list(filter(lambda x:x>=80,attendence_pct))
#print(attendence)
mid_term=list(filter(lambda x:x>=60,mid_term_scores))
#print(mid_term)
students_tup=list(zip(students,mid_term,end_term_scores))
print(students_tup)