transactions = [
    "  ord1 | books | python book | 400  ",
    "ORD2|BOOKS|C++ Guide|400",
    "ord3 | electronics | laptop | 1500",
    "ord4 | electronics | mouse | 1200",
    "invalid_transaction_entry",
]
list_trac=[i.split("|") for i in transactions]
up_list=[j for j in list_trac if len(j)==4]
print(up_list)
my_set={j.strip().upper() for i,j,k,l in up_list}
print("Categories:",my_set)
my_dict={
    cat:sorted([float(j[3].strip()) for j in up_list if j[1].strip().upper()==cat]) for cat in sorted(my_set)
}
#print(my_dict)
my_dict2={k:max(v)*90/100.0 for k,v in my_dict.items()}
print(my_dict2)