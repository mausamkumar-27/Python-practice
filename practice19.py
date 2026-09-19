d={}
s=set()
sentence=input("Enter sentence: ")
replace_space=sentence.replace(" ","")
for i in replace_space:
    s.update(replace_space)
#print(s)
vowel_set=set()
consonent_set=set()
for j in s:
    if j==('a','e','i','o','u','A','E','I','O','U'):
        vowel_set.update(j)
    else:
        consonent_set.update(j)

d['vowel']=d.get('vowel',set())+vowel_set
d['consonent']=d.get('consonent',set())+consonent_set
print(d)