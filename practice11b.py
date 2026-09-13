'''def validate_salaries(salary_dict):
    for i in salary_dict.items():
        if i.values()<=0:
            raise ValueError(f"Salary can't be zero or negative for {i}")
        if i.values()>500000:
            raise ValueError(f"Salary is unrealistically high for {i}")'''




def validate_salaries(salary_dict):
    for name,salary in salary_dict.items():
        if salary<=0:
            raise ValueError(f"Salary can't be zero or negative for {name}")
        if salary>500000:
            raise ValueError(f"Salary is unrealistically high for {name}")
        
        