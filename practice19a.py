

d={}
for i in range(1,4):
    names=input("Enter name: ")
    skill=set(input("Enter skills: ").split())
    d[names]=skill
#print(d)
#new_set=set((d.(values)).intersection(skill))      set ke andar immutable item hi jaayegi

#all_skills=set().union(*d.values())
#print("all_skills: " ,all_skills)   # ye * teeno set ko alag-2 open kiya & union leke set me daal diya
common_skills=list(d.values())[0].intersection(*d.values())
print("common_skills: ",common_skills)
'''summary={
    "common_skills":common_skills,
    "all_team_skills":all_skills
}
print(summary)'''