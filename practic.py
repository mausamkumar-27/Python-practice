# Write your code here...
n = int(input())
name_list = [input().strip() for i in range(1, n + 1)]
score_list = [int(input()) for j in range(1, n + 1)]
for name, score in zip(name_list, score_list):
  print(name, score)
score_set = {j for i, j in zip(name_list, score_list)}
updated_set = sorted(score_set, reverse=True)
updated_list = list(updated_set)
team = [
    i
    for i, j in zip(name_list, score_list)
    if updated_list[1] == j
]
print(sorted(team))