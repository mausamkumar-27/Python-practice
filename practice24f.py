employees=["Amit","Neha","Pooja","Rahul","Sneha"]
departments=["IT","HR","finance","IT","Marketing"]
ratings=[4.5,3.8,4.2,4.9,3.5]
base_salaries=[50000,45000,60000,75000,40000]
dictionary={emp:(bs*1.20 if r>=4.5 else bs*1.10) for emp,d,r,bs in zip(employees,departments,ratings,base_salaries) if r>4.0}
print(dictionary)