import os

# 1. Dekho ki aapka python script abhi kis folder ke andar chal raha hai
print("1. Current Working Directory:")
print(os.getcwd())

# 2. Is folder ke andar kitni files aur folders hain, unki list nikalo
print("\n2. Files and Folders in current directory:")
print(os.listdir())

# 3. Apne aap ek naya folder create karo code ke through
folder_name = "my_test_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"\n3. Folder '{folder_name}' successfully ban gaya!")
else:
    print(f"\n3. Folder '{folder_name}' pehle se hi wahan hai.")

# 4. Dubara check karo ki folder exist karta hai ya nahi
print("\n4. Does folder exist?", os.path.exists(folder_name))