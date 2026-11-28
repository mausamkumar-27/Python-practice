raw_records = [
    "  Math : 10 pts ",
    "invalid_record",
    "MATH: 5 PTS",
    " English : 8 pts",
    "english: 12 pts ",
    "Science: 20 pts",
    "history: 15",
    "  math : 3 pts ",
]

min_score = 4
filtered_list=list(filter(lambda x:":" in x and x.strip().lower().endswith("pts"),raw_records))
#print(filtered_list)
filtered_list2=list(map(lambda x:x.strip().lower().rstrip("pts"),filtered_list))
#print(filtered_list2)
filtered_list3=list(map(lambda x:x.strip().split(":"),filtered_list2))
#print(filtered_list3)
tup_list=[(i.strip(),int(j)) for i,j in filtered_list3]
#print(tup_list)
tup_sub=[i for i,j in tup_list]
#print(tuple(tup_sub))
if tup_sub.count("math")>0:
    i=tup_sub.index("math")
else:
    tup_list.append(("math",0))
#print(tup_list)
unique_sub={i for i,j in tup_list if i.isalpha()}
#print(unique_sub)
unique_sub.discard("science")
#print(unique_sub)
my_dict={key:[j for s,j in tup_list if j>=min_score and key==s] for key in sorted(unique_sub)}
#print(my_dict)
my_dict.setdefault("bonus",[5])
#print(my_dict)
b=my_dict.pop("bonus")
#print(my_dict)
#print(b)
def recursive_product(nums):
    if len(nums)==0:
        return 0
    elif len(nums)==1:
        return nums[0]
    else:
        return nums[0]*recursive_product(nums[1:])
prod_list=[recursive_product(s) for s in my_dict.values()]
print(prod_list)