n = int(input())
left = [] #x1y2
right = [] #y1x2
for i in range(n):
    inp = [ int(e) for e in input().split()]
    if i%2 == 0:
        left.append(inp[0])
        right.append(inp[1])
    else:
        left.append(inp[1])
        right.append(inp[0])
instruction = input()

mini = float('inf')
maxi = float('-inf')
if instruction == "Zig-Zag": 
    #find min of left, max of right
    for i in range(n):
        mini = min(mini,left[i])
        maxi = max(maxi,right[i])
elif instruction == "Zag-Zig":
    #find max of left, min of right
    for i in range(n):
        maxi = max(maxi,left[i])
        mini = min(mini,right[i])
print(mini,maxi)