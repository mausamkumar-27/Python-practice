class scientificcalc:
    def square(self,n):
        result=n**2
        print(f"Square:{result}")
    def cube(self,n):
            result=n**3
            print(f"Cube:{result}")
    def square_root(self,n):
            result=n**0.5
            print(f"Square root:{result}")
cal=scientificcalc()
cal.square(2)
cal.cube(3)
cal.square_root(81)    
