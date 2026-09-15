'''import os
current_dir=os.getcwd()
print("Current Directory: ",current_dir)

import os
items=os.listdir()
print(items)

import os
if not os.path.exists("test_dir"):
    os.mkdir("test_dir")
    print("Directory created is successfully!")

import os
os.rename("test_dir","retest_dir")

import os
os.rmdir("retest_dir")'''            #lo ye file delete bhi kr diya


import os 
if os.path.exists("virtual_envy.py"):
    print("The file exists!")
    