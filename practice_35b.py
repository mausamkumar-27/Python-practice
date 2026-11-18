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
            print(f"{self.room_name} temperature set to {new_temp}")