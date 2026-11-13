class student_report:
    def set_marks(self,name,maths,science):
        self.name=name
        self.maths=maths
        self.science=science
    def display_info(self):
        print(f"Studnet Name:{self.name}")
        print(f"Math Marks:{self.maths}")
        print(f"Science Marks:{self.science}")
    def calculate_total(self):
        total=self.maths + self.science
        print(f"Total Marks:{total}")
report=student_report()
report.set_marks("Mausam",90,95)
report.display_info()
report.calculate_total()