ball = { 'X':0,'R':1, 'Y':2, 'G':3, 'W':4, 'B':5, 'P':6, 'K':7 }

score = [0,0,0]
R = 0

#first half
while True:
    inp = input()
    if 'X' in inp:
        if len(inp) == 3 and inp[2] == 'X':
            score[int(inp[0])] += ball[inp[1]]
            R += 1
    else:
        score[int(inp[0])] += ball[inp[1]] + ball[inp[2]]
        R += 1
    #print("R is",R)
    if R >= 6:
        break

#second half
while True:
    inp = input()
    score[int(inp[0])] += ball[inp[1]]
    if inp[1] == 'K':
        break

print(score[1],score[2])
if score[1] > score[2]:
    print("Player 1 wins")
elif score[1] < score[2]:
    print("Player 2 wins")
else:
    print("Tie")
#23 min