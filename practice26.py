from functools import reduce
students=["Aman","Priya","Rohan","Divya","Karan"]
attendence_pct=[85,92,78,95,60]
mid_term_scores=[70,88,55,90,45]
end_term_scores=[75,92,60,94,50]
students_tup=list(zip(students,attendence_pct,mid_term_scores,end_term_scores))
my_dict={name:(mid+end)/2 for name,att,mid,end in students_tup if att>=80 and mid>=60}
#print(my_dict)
my_dict_values=list(my_dict.values)
print(my_dict_values)
total_sum= reduce(lambda x,y:x+y,my_dict_values)
print("Eligible Students Dictionary:",my_dict)
print("Total Sum of Eligible Scores:",my_dict_values)