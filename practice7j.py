sentence="Python Programming is Awasome"
print(sentence.lower())
vowels="aeiou"
count=0
for char in sentence:
    if char in vowels:
        count+=1
        