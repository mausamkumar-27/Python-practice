for i in range(6):
    print(i)
else:
    print("Loop finished successfully!")


for i in range(7):
    print(i)
    if i==4:
        break
else:
    print("This will not execute!")

for i in []:
    print(i)
else:
    print("Execute even an empty iterable!")