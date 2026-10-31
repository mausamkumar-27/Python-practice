from functools import reduce
Names="amit,rohit,priya,sneha"
Salaries="40000,50000,60000,45000"
Departments="HR,IT,Finance,IT"
Bonus=15
list_names=Names.split(",")
#print(list_names)
list_salaries=list(map(int,Salaries.split(",")))
#print(list_salaries)
list_departments=Departments.split(",")
my_dict={name:(department,(salary*115)/100) for name,department,salary in zip(list_names,list_departments,list_salaries)}
#print(my_dict)
final_salary=list(map(lambda x:(x*115)/100 ,list_salaries))
total_revenue=reduce(lambda x,y:x+y,final_salary)
#print(total_revenue)
for name,details in my_dict.items():
    department,final_salaries=details
    print(f"Employee:{name.strip().capitalize()} | Department:{department.strip().upper()} | Total Salary:{final_salaries}")
print(f"Total Company Payroll Expenditure:{total_revenue}")