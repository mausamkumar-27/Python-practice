def calculate_total_earnings(emp_name,base_salary,bonus=3000,*extra_incentives):
    return base_salary+bonus+sum(extra_incentives)
r1=calculate_total_earnings("Mausam",25000,3000,200,100,900)
print("Your total earnings is: ",r1)