try:
    arr=[10,20]
    print(arr[1])
except ValueError:
    print("Handled ValueError")
finally:
    print("Closing active connection before system crash...")