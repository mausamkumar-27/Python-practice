from functools import reduce
def process_payroll(employees_list,active_dept_set,bonus_criteria_func):
    cleaned_employees=[]
    for emp in employees_list:
        emp_copy=emp.copy()
        emp_copy['name']=emp_copy['name'].strip().title()
        cleaned_employees.append(emp_copy)

       #print(emp)
    print(cleaned_employees)

    filtered_emps=list(filter(lambda emp: emp['dept'] in active_dept_set,cleaned_employees))

    updated_emps=list(map(lambda emp:{
        **emp,
        'salary':round(emp['salary']*1.15,2)if bonus_criteria_func (emp['skills']) else round(emp['salary']*1.05,2)
    },filtered_emps))

    total_salary=reduce(lambda acc,emp:acc+emp['salary'],updated_emps,0.0)
    depts={emp['dept'] for emp in updated_emps}

    dept_salary_mapping={
        dept: sorted([emp['salary'] for emp in updated_emps if emp['dept']==dept],reverse=True) for dept in depts
    }

    return {
        "Total_Salary_Expense":total_salary,
        "Dept_Salary_Mapping":dept_salary_mapping
    }
employees = [
    {"name": "  mausam kumar ", "dept": "Engineering", "salary": 50000, "skills": ["Python", "C++", "DSA"]},
    {"name": "rohit sharma", "dept": "HR", "salary": 30000, "skills": ["Communication"]},
    {"name": "  amit singh", "dept": "Engineering", "salary": 60000, "skills": ["Python", "AI", "ML"]},
    {"name": "priya roy", "dept": "Finance", "salary": 45000, "skills": ["Excel", "Python"]}
    ]
active_depts = {"Engineering", "Finance"}
criteria=lambda skills:len(skills)>=3
print(process_payroll(employees,active_depts,criteria))