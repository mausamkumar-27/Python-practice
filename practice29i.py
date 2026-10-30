class studentexam:
    def set_student(self,name,marks):
        self.name=name
        self.marks=marks
    def check_result(self):
        if self.marks >=40:
            print(f"Student {self.name}:Pass (Marks:{self.marks})")
        else:
            print(f"Student {self.name}:Fail (Marks:{self.marks})")
r1=studentexam()
r2=studentexam()
r1.set_student("Mausam",95)
r2.set_student("Hardik",28)
r1.check_result()
r2.check_result()