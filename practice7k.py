tagline="artificial intelligence and machine learning"
a=tagline.replace("and","&")
print(a)
b=tagline.split()
print(b)
acronym=""
for i in b:
    acronym+= i[0].upper()
print("Acronym: ",acronym)

    