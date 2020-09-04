sol = input()
ans = input()

if len(sol) != len(ans):
    print("Incomplete answer")
else:
    n = len(sol)
    score = 0
    for i in range(n):
        if ans[i] == sol[i]:
            score += 1
    print(score)