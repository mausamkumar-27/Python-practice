class student:
    def __init__(self):
        self._marks=50
    @property
    def marks(self,new_marks):
        if new_marks <0 or new_marks>100:
            print("Error:Marks must be between 0 and 100!")
        else:
            self._marks=new_marks
            print("Marks updated successfully!")
s1=student()
s1._marks=120
print(s1.marks)