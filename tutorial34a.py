original={'a':1,'b':2}
copied_dict=original.copy()
#nyi dict bni ab isme tu changes kr skte ho
copied_dict['a']=99
print(copied_dict)
print(original)



info={'name':'Mausam Kumar'}
age=info.setdefault('age',18)
print(info)