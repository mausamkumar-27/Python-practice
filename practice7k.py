tagline="artificial intelligence and machine learning"
print(tagline.replace("and","&"))
a=tagline.split()
print(a)
acronym=""
for i in a:
    acronym+= i[0].upper()

    