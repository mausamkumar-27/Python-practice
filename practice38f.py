n = int(input())
raw_lines = [input().split() for i in range(n)]
teams = [(name, int(score)) for name, score in raw_lines]
print(teams)

'''unique_scores = sorted({score for _, score in teams}, reverse=True)
second_highest = unique_scores[1]

runners_up = sorted(name for name, score in teams if score == second_highest)
print(", ".join(runners_up))'''