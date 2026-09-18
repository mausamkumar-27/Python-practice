def user(*names):
    d={}
    vowel_list=[]
    consonant_list=[]
    for i in names:
        if i[0].lower() in ('a','e','i','o','u'):
            vowel_list.append(i)
        else:
            consonant_list.append(i)
    d['vowel']=tuple(vowel_list)
    d['consonant']=tuple(consonant_list)
    print(d)
user('Mausam','hardik','ram','Utthappa','Elvish','Aman')