class smartphone:
    def set_specs(self,brand,ram,storage):
        self.brand=brand
        self.ram=ram
        self.storage=storage
    def show_specs(self):
        print(f"Brand:{self.brand},RAM:{self.ram},Storage:{self.storage}")
phone1=smartphone()
phone2=smartphone()
phone1.set_specs("Samsung","8GB","128GB")
phone2.set_specs("OnePlus","12GB","256GB")
phone1.show_specs()
phone2.show_specs()