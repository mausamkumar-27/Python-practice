list=[5,7,9,11]

try:
    print(list[5])

except IndexError:
    print("Your index is out of range")
finally:
    print("This block will always run !")