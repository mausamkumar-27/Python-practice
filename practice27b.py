warehouse_stock=500
def view_stock():
    print("Available Stock:",warehouse_stock)
def sell_stock(quantity):
    global warehouse_stock
    warehouse_stock -=quantity
    print("Stock after selling:",warehouse_stock)
def add_stock(quantity):
    global warehouse_stock
    warehouse_stock +=quantity
    print("Stock after adding:",warehouse_stock)
view_stock()
sell_stock(120)
add_stock(300)
view_stock()
print("Stock outside functions:",warehouse_stock)