raw_inputs=["45","100","twenty","80","N/A","95"]
valid_numbers=[]
for items in raw_inputs:
    print(items)
try:
    new=int(items).valid_number.append()
    print(new)

except ValueError:
    print(f"skipping invalid:{items}")
print(valid_numbers)

