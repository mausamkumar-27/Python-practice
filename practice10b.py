def validate_grades(grade_dict):
    d={}
    for name,mark in grade_dict.items():
        if mark<0 or mark>100:
            raise ValueError(f"Please! Enter valid marks")
    try:
        validate_grades({"Mausam":85,"Aman":90,"Priya":95,"Raman":120,"Chaman":-10})
    except ValueError as e:
        print("Caught error:",e)


        