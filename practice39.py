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
print(tup_list)
tup_sub=[i for i,j in tup_list]
print(tuple(tup_sub))
tup1=tuple(i for i in tup_sub)
print(tup1)