from functools import reduce
students=["Aman","Priya","Rohan","Divya","Karan"]
attendence_pct=[85,92,78,95,60]
mid_term_scores=[70,88,55,90,45]
end_term_scores=[75,92,60,94,50]
all_tup=list(zip(students,attendence_pct,mid_term_scores,end_term_scores))
#print(all_tup)
my_dict={name:(mt+et)/2 for name,att,mt,et in all_tup if att>=80 and mt>=60}
total_sum=reduce(lambda x,y:x+y,my_dict.values())
print("Eligible Students Dictionary:",my_dict)
print("Total Sum of Eligible Scores:",my_dict.values())