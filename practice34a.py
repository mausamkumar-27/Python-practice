#from functools import reduce
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
