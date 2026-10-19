s="Learning Python is fun and exciting."
s=s.lower()
vowels="aeiou"
vowel_counts=0
consonent_counts=0
for i in s:
    if i.isalpha():
        if i in vowels:
            vowel_counts+=1
        else:
            consonent_counts+=1
print(f"Total vowels:{vowel_counts}")
print(f"Total consonants:{consonent_counts}")