'''class MathsUtils:
    @staticmethod
    def add(a,b):
        return a+b
#obj=MathsUtils()
result=MathsUtils.add(10,20)
print(f"Sum:{result}")'''

class TemperatureConverture:
    def __init__(self,city_name,temp_celsius):
        self.city_name=city_name
        self.temp_celsius=temp_celsius
    @staticmethod
    def Fahren(c):
        return (c*9/5) +32
    