from functools import reduce
employees = [
    {"name": " priya das ", "dept": "Operations", "salary": 38000, "skills": ["Excel", "SQL", "Python"]},
    {"name": "vikram singh", "dept": "HR", "salary": 30000, "skills": ["Communication"]},
    {"name": " pooja mehta ", "dept": "Operations", "salary": 52000, "skills": ["SQL", "Tableau", "Python", "PowerBI"]},
    {"name": "rahul verma", "dept": "Finance", "salary": 45000, "skills": ["Tally", "Excel"]}
]

active_depts = {"Operations", "Finance"}

criteria = lambda skills: len(skills) >= 3

cleaned_emp=list(map(lambda emp:{**emp, "name":emp["name"].strip().title()},employees))
#print(cleaned_emp)
filtered_emps=list(filter(lambda item:item["dept"] in active_depts,cleaned_emp))
#print(filtered_emps)
updated_emps=list(map(lambda x:{
    **x,"salary":round(x["salary"]*1.15,2 )if criteria(x["skills"]) else round(x['salary']*1.05,2)
},filtered_emps))
#print(updated_emps)
total_salary=reduce(lambda x,y:x+y["salary"],updated_emps,0)
print("Total Salary:",total_salary)
depts={i["dept"] for i in updated_emps}
#print(depts)
dept_salary_mapping = {
    d: sorted([j["salary"] for j in updated_emps if j["dept"] == d], reverse=True)
    for d in depts
}
print(dept_salary_mapping)