inventory={
    "Apple":(120,15),        #price,stock
    "Banana":(40,0),
    "Mango":(80,25),
    "Orange":(60,0)
}
out_of_stock=set()
total_value=0
for fruit,(price,stock) in inventory.items(): 
    print(fruit,(price,stock))
    if(stock==0):
        out_of_stock.add(fruit)
        print(out_of_stock)
    total_value+=price*stock
    print(total_value)