n = int(input())

# 1. Upper Half
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    for k in range(1, 2 * (n - i) + 1):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# 2. Lower Half
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    for k in range(1, 2 * (n - i) + 1):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()