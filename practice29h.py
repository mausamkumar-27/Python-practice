class shopingcart:
    def add_item(self,item_name,price):
        self.item_name=item_name
        self.price=price
    def show_bill(self):
        print(f"Item:{self.item_name},Price:{self.price}")
cart1=shopingcart()
cart2=shopingcart()
cart1.add_item("MacBook-M5",120000)
cart2.add_item("POCO X6 PRO",26000)
cart1.show_bill()
cart2.show_bill()