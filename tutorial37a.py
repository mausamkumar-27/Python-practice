try:
    arr=[10,20]
    print(arr[9])
#except ValueError:
except IndexError:
    print("Handled ValueError")
finally:
    print("Closing active connection before system crash...")