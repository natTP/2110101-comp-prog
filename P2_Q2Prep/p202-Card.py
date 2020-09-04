cardVal = { 'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10,'J':11,'Q':12,'K':13 }
cardSym = { 'C':1, 'D':2, 'H':3, 'S':4 }

inp = input()
card = []
for i in range(0,len(inp),2):
    card.append(inp[i:i+2])

ans = ""
for i in range(len(card)-1):
    if card[i] == card[i+1]:
        ans += '0'
    elif card[i][0] == card[i+1][0]:
        diff = cardSym[card[i][1]] - cardSym[card[i+1][1]]
        if diff <= 0:
            ans += str(diff)
        else:
            ans += '+' + str(diff)
    else:
        diff = cardVal[card[i][0]] - cardVal[card[i+1][0]]
        if diff <= 0:
            ans += str(diff)
        else:
            ans += '+' + str(diff)       
print(ans)

#13 min