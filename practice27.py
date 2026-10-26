'''store_name="SuperMart"
def display_store():
    print("Global inside display_store:",store_name)
def local_discount():
    store_name="LocalMart"
    print("Local inside local_discount:",store_name)
display_store()
local_discount()
print("Global outside function:",store_name)'''

passing_marks=40
def check_default_passing():
    print("Global output aayegi:",passing_marks)
def stict_evaluations():
    passing_marks=60
    print("Local output aayegi:",passing_marks)
check_default_passing()
stict_evaluations()
print("Yahan bhi global output aayegi:",passing_marks)