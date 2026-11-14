from functools import reduce
def process_payroll(employees_list,active_dept_set,bonus_criteria_func):
    cleaned_employees=[]
    for emp in employees_list:
        emp_copy=emp.copy()
        emp_copy['name']=emp_copy['name'].strip().title()
        cleaned_employees.append(emp_copy)

    filtered_emps=list(filter(lambda emp: emp['dept'] in active_dept_set,cleaned_employees))

    updated_emps=list(map(lambda emp:{
        **emp,
        'salary':emp['salary']*1.15 if bonus_criteria_func (emp['skills']) else emp['salary']*1.05
    },filtered_emps))

    total_salary=reduce(lambda acc,emp:acc+emp['salary'],updated_emps,0.0)
    depts={emp['dept'] for emp in updated_emps}

    dept_salary_mapping={
        dept: sorted([emp['salary'] for emp in updated_emps if emp['dept']==dept],reverse=True) for dept in depts
    }

    return {
        "Total_Salary_Expanse":total_salary,
        "Dept_Salary_Mapping":dept_salary_mapping
    }

criteria=lambda skills:len(skills)>=3
print(process_payroll(employees,active_depts,criteria))