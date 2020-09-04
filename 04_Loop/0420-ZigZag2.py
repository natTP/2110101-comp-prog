minL = float('inf')
maxL = float('-inf')
minR = float('inf')
maxR = float('-inf')

inp = input()
i = 0
while inp != "Zig-Zag" and inp != "Zag-Zig":
    L = int(inp.split()[0])
    R = int(inp.split()[1])
    if i%2 == 0:
        minL = min(minL,L)
        maxL = max(maxL,L)
        minR = min(minR,R)
        maxR = max(maxR,R)
    else:
        minL = min(minL,R)
        maxL = max(maxL,R)
        minR = min(minR,L)
        maxR = max(maxR,L)
    i += 1
    inp = input()
if inp == "Zig-Zag":
    print(minL,maxR)
elif inp == "Zag-Zig":
    print(minR,maxL)