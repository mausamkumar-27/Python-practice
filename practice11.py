def process_mixed_data(data_list):
    s=set()
    for i in data_list:
        s.update(i)
        print(s)


process_mixed_data(("Mausam","Hardik","Aman"))