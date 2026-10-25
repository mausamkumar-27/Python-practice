from functools import reduce
applicants=["Aarav","Pooja","Rohan","Simran","Kabir"]
credit_scores=[780,650,720,590,810]
loan_amounts=[500000,300000,750000,200000,1000000]
employment_types=["Salaried","Business","Salaried","Freelancer","Salaried"]
tenure_years=[5,3,4,2,7]
final_loan_cost=list(map(lambda loan,credit,tenure:(loan*tenure*0.08)+(0 if credit>= 750 else(2000 if 700<=credit <749 else(5000 if 650<=credit<699 else 10000))),loan_amounts,credit_scores,tenure_years))
my_dict={name:cost for name,cost,final_loan,c_s in zip(applicants,final_loan_cost,loan_amounts,credit_scores) if c_s>=700 and final_loan>=400000}
reduce_dict=(reduce(lambda x,y:x+y,my_dict.values())/len(my_dict) if len(my_dict)>0 else 0)
print(my_dict)
print(reduce_dict)