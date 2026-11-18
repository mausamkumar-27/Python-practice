class Mobile:
    def __init__(self):
        self._battery=80
    @property
    def battery(self):
        return self._battery
    @battery.setter
    def battery(self,new_level):
        if new_level<0 or new_level>100:
            print("Error:Battery 0 to 100 ke beeech honi chahiye!")
        else:
            self._battery=new_level
            print("Battery level updated!")
phone=Mobile()
phone.battery=150
phone.battery=45
print(phone.battery)