def process_mixed_data(data_list):
    s=set()
    for i in data_list:
        #s.update(i)
        #s.add(i)           #add uses for single element only--haan for loop me i single element hi hai
    
        try:
            val=int(i)
            s.add(val)
        except ValueError:
            print(f"skkiping invalid integer!")
    print(s)
process_mixed_data(("Mausam",9,122,122,9,7,56,7,"Hardik","Aman"))