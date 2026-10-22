students=["Mausam","Rahul","Aman"]
marks_tuple=((85,90,88),(78,82,80),(92,95,90))
'''avg_list=[]
for i in marks_tuple:
    avg=sum(i)/len(i)
    #print(avg)
    avg_list.append(avg)
#print(avg_list)
my_dict=dict(zip(students,avg_list))
print(my_dict)'''

avg_list=[sum(i)/len(i) for i in marks_tuple]
#print(avg_list)
my_dict=dict(zip(students,avg_list))
print(my_dict)
