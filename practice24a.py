students=["Mausam","Rahul","Aman"]
marks_tuple=((85,90,88),(78,82,80),(92,95,90))
avg_list=[]
for i in marks_tuple:
    avg=sum(i)/len(i)
    #print(avg)
    b=avg_list.union(avg)
    print(b)