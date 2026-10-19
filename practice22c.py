basic_salary=int(input("Enter your basic Salary: "))
bonus=int(input("Enter bonus: "))
def calculate_net_salary(basic_salary,bonus):
    return basic_salary+bonus
result1=calculate_net_salary(basic_salary,bonus)
result2=calculate_net_salary(basic_salary,1000)
print(result1)
print(result2)
