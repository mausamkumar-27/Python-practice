languages=["Python","C","C++","Java"]
idx=int(input("Enter index to search:"))
try:
    print(languages[idx])
except IndexError:
    print("Index out of bounds! valid range is 0 to 3")
