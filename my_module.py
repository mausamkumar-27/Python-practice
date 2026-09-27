def welcome():
    print("Welcome to Python programming,Mausam!")
if __name__ == "__main__":
    print("Running directly from my_module.py")
    welcome()
else:
    print("Imported from another file")

print("Current __name__ value is:",__name__)