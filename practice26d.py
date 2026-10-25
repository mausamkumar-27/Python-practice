restaurants=["Spicy Hut","Burger King","Pizza Oven","Tandoori Nights","South Spice"]
categories=["Fast Food","Fast Food","Italian","North Indian","South Indian"]
avg_prices=[250,180,400,350,200]
items_sold=[120,200,90,70,150]
ratings=[4.6,3.8,4.4,3.5,4.7]
final_revenue=list(map(lambda price,sold,cat:(price*sold)+(2000 if cat=="Italian" else (1500 if cat=="North Indian" else (1000 if cat=="Fast Food" else 800)))))
