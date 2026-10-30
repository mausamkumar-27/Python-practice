class studentexam:
    def set_student(self,name,marks):
        self.name=name
        self.marks=marks
    def check_result(self):
        if marks >=40:
            print(f"Student {self.name}:Pass (Marks:{self.marks})")
        else:
            print(f"Student {self.name}:Fail (Marks:{self.marks})")