wota = {} #wname:{idol:v}
idolvotes = {} #idol:score
wofi = {} #idol:[list of wname] #USING A SET WOULD BE BETTER; NO NEED TO CHECK EXISTENCE

inp = input()
while inp not in ['1','2','3']:
    wname, idol, v = inp.split()
    if wname not in wota:
        wota[wname] = {}
    if idol in wota[wname]:
        wota[wname][idol] += int(v)
    else:
        wota[wname][idol] = int(v)
    if idol in idolvotes:
        idolvotes[idol] += int(v)
    else:
        idolvotes[idol] = int(v)
    if idol not in wofi:
        wofi[idol] = []
    if wname not in wofi[idol]:
        wofi[idol].append(wname)
    inp = input()
    
#print(wota)
#print(idolvotes)
#print(wofi)

if inp == '1': #by votes
    iv = sorted([ (-v,idol) for idol,v in idolvotes.items() ])
    print(", ".join([ idol for v,idol in iv ][:3]))
    
elif inp == '2': #by num of wota
    nw = sorted([ (-len(wotas), idol) for idol,wotas in wofi.items() ])
    print(", ".join([ idol for wotas,idol in nw ][:3]))
    
elif inp == '3': #by kami
    kami = {} #idol:[list of w] #USING A SET WOULD BE BETTER
    for i in idolvotes:
        kami[i] = []
    for w in wota:
        oshi = sorted([ (-v,idol) for idol,v in wota[w].items() ])
        kami[oshi[0][1]].append(w)
    nk = sorted([ (-len(wotas), idol) for idol,wotas in kami.items() ])
    print(", ".join([ idol for wotas,idol in nk ][:3]))
    