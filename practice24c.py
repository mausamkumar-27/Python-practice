products=["Laptop","Smartphone","Headphones"]
prices=[50000,20000,2500]
discounts=[10,15,5]
b=list(zip(prices,discounts))
new_prices=[]
for p,d in b:
    c=p-(p*d)/100
    new_prices.append(c)
print(new_prices)