
orders = [
    {"customer": " amit sharma ", "category": "Electronics", "amount": 15000, "items": 4},
    {"customer": "Priya singh", "category": "Apparel", "amount": 3500, "items": 2},
    {"customer": " rohit verma ", "category": "Electronics", "amount": 25000, "items": 5},
    {"customer": "neha gupta", "category": "Groceries", "amount": 2000, "items": 6}
]
active_categories = {"Electronics", "Apparel"}
discount_criteria = lambda items: items >= 3

cleaned_orders=list(map(lambda name:{
    **name,"customer":name["customer"].strip().title()
},orders))
#print(cleaned_orders)