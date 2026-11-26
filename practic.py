# Write your code here...
'''n = int(input())
name_list = [input().strip() for i in range(1, n + 1)]
#print(*name_list)
score_list = [int(input()) for j in range(1, n + 1)]
#print(*score_list)
for name, score in zip(name_list, score_list):
  print(name, score)
score_set = {j for i, j in zip(name_list, score_list)}
#print(score_set)
updated_set = sorted(score_set, reverse=True)
#print(updated_set)
updated_list = list(updated_set)
#print(updated_list)
team = [i for i, j in zip(name_list, score_list) if updated_list[1] ==j ]
print(*sorted(team),sep=", ")'''
'''s=input()
vowel="AEIOUaeiou"
d={i:s.count(i) for i in s if i in vowel}
print(d)'''

n=[int(i) for i in input().strip().split()]
m=min(n)
M=max(n)
#print(M,m)
print(M-n)
