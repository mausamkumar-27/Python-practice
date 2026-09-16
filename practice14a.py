list_of_tuple=[]
d={}
for i in range(1,6):
    string_name=input("Enter name: ")
    score=int(input("Enter score: "))
    list_of_tuple.append((string_name,score))
print(list_of_tuple)
for string_name,score in list_of_tuple:
    if len(string_name)>3:
        d[string_name]=score
print(d)