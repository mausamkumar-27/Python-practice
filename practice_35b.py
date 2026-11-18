class Thermostat:
    def __init__(self,room_name,initial_temp=24):
        self.room_name=room_name
        self._temperature=initial_temp
    @property
    def temperature(self):
        return self._temperature
    @temperature.setter
    def temperature(self,new_temp):
        if new_temp<16 or new_temp>30:
            print("Alert:Temperature 16 to 30 ke beech honi chahiye!")
        else:
            self._temperature=new_temp
            print(f"{self.room_name} temperature set to {new_temp}°C")
t1=Thermostat("Bedroom",22)
print(f"{t1.room_name} initial temp:{t1.temperature}°C")
t1.temperature=35
t1.temperature=16
print(f"{t1.room_name} final temp:{t1.temperature}°C")
t2=Thermostat("Livingroom")
print(f"{t2.room_name} default temp:{t2.temperature}°C")