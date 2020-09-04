result = input().strip()

framescore = [0]*11
ttlscore = 0
i = 0

for f in range(1,11):
    if result[i:i+3] == "XXX":  #XXX
        framescore[f] = 30
        i += 1
    elif result[i:i+2] == "XX": #XX?
        framescore[f] = 20 + int(result[i+2])
        i += 1
    elif result[i] == "X":
        if result[i+2] == "/":  #X?/
            framescore[f] = 20
        else:                   #X??
            framescore[f] = 10 + int(result[i+1]) + int(result[i+2])
        i += 1
    elif result[i+1] == "/":     
        if result[i+2] == "X":  #?/X 
            framescore[f] = 20
        else:                   #?/?
            framescore[f] = 10 + int(result[i+2])
        i += 2
    else:
        framescore[f] = int(result[i]) + int(result[i+1])   #??
        i += 2
    ttlscore += framescore[f]

q = int(input())
if q in range(1,11):
    print(framescore[q])
else:
    print(ttlscore)