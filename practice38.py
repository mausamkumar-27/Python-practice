entries = [
    "  m101 | eng | 15, 25, 15, 40  ",
    "M102|ENG|20, 15, 20",
    "m201 | ops | 10, 30, 50, 30",
    "invalid_record_here",
]
entries_list=[i.strip().split("|") for i in entries]
#print(entries_list)
up_list=[j for j in entries_list if len(j)==3]
print(up_list)
my_dict={j.upper():k.split() for i,j,k in up_list}
print(my_dict)