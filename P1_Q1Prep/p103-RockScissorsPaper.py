m = int(input())
win = [0,0]

tie = True
for i in range(3*m):
    rps = input().split()
    if rps == ['R','P']:
        win[1] += 1
    elif rps == ['P','R']:
        win[0] += 1
    elif rps == ['P','S']:
        win[1] += 1
    elif rps == ['S','P']:
        win[0] += 1
    elif rps == ['S','R']:
        win[1] += 1
    elif rps == ['R','S']:
        win[0] += 1
    if win[0] >= m:
        tie = False
        print(win[0],win[1])
        print("Player 1 wins")
        break
    elif win[1] >= m:
        tie = False
        print(win[0],win[1])
        print("Player 2 wins")
        break
if tie:
    print(win[0],win[1])
    print("Tie")