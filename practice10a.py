def extract_unique_integer(data_tuple):
    s=set()
    for i in data_tuple:
        print(i)
extract_unique_integer(("Mausam",2,2.7,10,2,10,"Hello"))      #tumne kevl 1 parameter liye ho line 1 me isliye double (()) taaki ek tuple lge
try:
    a=int(i)
except ValueError:
    print("control the error")
s.update(a)
print(s)

    