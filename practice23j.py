group1={"Mausam","Rahul","Amit","Karan"}
group2={"Amit","Sneha","Vikas","Rohit"}
group3={"Karan","Sneha","Vikas","Rohit"}

#print("All members of g1 & g2:",group1.union(group2))
all_members=group1.union(group2)
print(all_members)
#print(group1.update(group2))
group1.update(group2)
print(group1)
