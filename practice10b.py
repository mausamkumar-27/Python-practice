def validate_grades(grade_dict):
    d={}
    for name,mark in grade_dict.item():
        if mark<0 or mark>100:
            raise ValueError(f"Please! Enter valid marks")
        