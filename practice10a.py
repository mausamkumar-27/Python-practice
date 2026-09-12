def extract_unique_integer(data_tuple):
    s=set()
    for i in data_tuple:
        try:
            a=int(i)
            s.add(a)
        except ValueError:
            print("control the Error")
    print(s)
extract_unique_integer(("Mausam",2,2.7,10,2,10,5,7,8,"Hello"))      #tumne kevl 1 parameter liye ho line 1 me isliye double (()) taaki ek tuple lge
