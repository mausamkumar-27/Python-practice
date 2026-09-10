numbers=[10,25,45,80,95]
target=50
for i in numbers:
    if i==50:
        print(f"found{target}")
        break
else:
    print(f"{target} not found")





numbers=[10,25,45,80,95]
target=100
found=False
for num in numbers:
    if num==target:
        found=True
        print(f"found{target}")

if not found:
    print(f"{target} not found!")




