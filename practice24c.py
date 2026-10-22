products=["Laptop","Smartphone","Headphones"]
prices=[50000,20000,2500]
discounts=[10,15,5]
new_prices=[]
for i in prices:
    for j in discounts:
        b=i-(i*j)/100
        new_prices.append(b)
print(new_prices)