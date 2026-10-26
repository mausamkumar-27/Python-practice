store_name="SuperMart"
def display_store():
    print("Global inside display_store:",store_name)
def local_discount():
    store_name="LocalMart"
    print("Local inside local_discount:",store_name)
display_store()
local_discount()
print("Global outside function:",store_name)