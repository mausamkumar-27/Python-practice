correct_pin=1234
attempts=3
while attempts > 0:
    entered_pin =int(input("Enter PIN: "))
    if entered_pin==correct_pin:
        print("Access Granted")
    else:
        attempts-=1
        print("Wrong PIN! Attempts Left: ",attempts)
if attempts==0:
    print("Account Locked")