day=input("Enter day name: ")
match day:
    case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
        print("Weekday:Time to work!")
    case "Saturday"|"Sunday":
        print("Weekend:Time to relax!")
    case _:
        print("Invalid Day!")