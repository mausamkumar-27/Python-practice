languages=["Python","C","C++","Java"]
idx=input("Enter index to search:")
try:
    print(languages[int(idx)])
#except (ValueError,IndexError,TypeError):
    #print("Index out of bounds! valid range is 0 to 3")


except IndexError:
     print("Index out of bounds! valid range is 0 to3")
except ValueError:
    print("Enter numbers only!")
