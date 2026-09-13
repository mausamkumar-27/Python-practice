def check_age(age_dict):
    for name,age in age_dict.items():
        if age <0:
            raise ValueError("Agel must be greater than zero")
        if age!=int(age) or age!=float(age):
            raise ValueError("Age must be valid Number")
    try:
        check_age({"Rahul":25,"Priya":-5.9,"Amit":-3})
    except ValueError:
        print(f"Enter positive no only")
    except TypeError:
        print("Age must be valid no")
