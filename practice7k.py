tagline="artificial intelligence and machine learning"
tagline=tagline.replace("and","&")
print(tagline)
b=tagline.split()
print(b)
acronym=""
for i in b:
    acronym+= i[0].upper()
print("Acronym: ",acronym)

    