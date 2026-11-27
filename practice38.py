transactions = [
    "  ord1 | books | python book | 400  ",
    "ORD2|BOOKS|C++ Guide|400",
    "ord3 | electronics | laptop | 1500",
    "ord4 | electronics | mouse | 1200",
    "invalid_transaction_entry",
]
list_trac=[i.split("|") for i in transactions]
up_list=[j for j in list_trac if len(j)==4]
#print(up_list)
my_dict={j.strip().upper():float(l)*90/100.0 for i,j,k,l in up_list}
print(my_dict)