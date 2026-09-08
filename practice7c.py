inventory={
    "Apple":(120,15),        #price,stock
    "Banana":(40,0),
    "Mango":(80,25),
    "Orange":(60,0)
}
out_of_stock=set()
for item in inventory:
    print(item)