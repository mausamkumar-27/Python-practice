def get_day_name(day_number):
    match day_number:
        case 1 :
            return "Monday "
        case 2 :
            return "Tuesday "
        case 3 :
            return "Wednesday "
        case 4 :
            return "Thursday "
        case 5 :
            return "Friday "
        case 6 :
            return "Saturday "
        case 7 :
            return "Sunday "
        case _ :
            return "Please! Enter valid number"
r1=get_day_name(7)
r2=get_day_name(4)
r3=get_day_name(3)
r4=get_day_name(10)
print(r1)
print(r2)
print(r3)
print(r4)