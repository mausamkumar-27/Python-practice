correct_pin=1234
attempts=3
while attempts > 0:
    entered_pin =int(input("Enter PIN: "))
    if entered_pin==correct_pin:
        print("Access Granted")