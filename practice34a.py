from functools import reduce
products = [
    {"name": " wireless mouse ", "category": "Electronics", "price": 800, "stock": 45},
    {"name": "notebook", "category": "Stationery", "price": 120, "stock": 8},
    {"name": " mechanical keyboard ", "category": "Electronics", "price": 3500, "stock": 12},
    {"name": " gel pen set ", "category": "Stationery", "price": 150, "stock": 60}
]
active_categories = {"Electronics", "Stationery"}
pricing_criteria = lambda stock: stock >= 20

cleaned_products=list(map(lambda x:{
    **x,
    "name":x["name"].strip().title()
},products))
#print(cleaned_products)
filtered_products=list(filter(lambda y:y["category"] in active_categories,cleaned_products))
#print(filtered_products)
updated_products=list(map(lambda z:{
    **z,
    "price":round(z["price"]*0.90,2) if z["stock"]>=20 else round(z["price"]*0.95,2)
},filtered_products))
#print(updated_products)
total_sum=reduce(lambda x,y:x+y["price"],updated_products,0)
print("Total Sum:",total_sum)