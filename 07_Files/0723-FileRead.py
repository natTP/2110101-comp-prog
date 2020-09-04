#import os
#print("Current Working Directory: " + os.getcwd())

file,query = input().split()
data = open(file,"r")

mini = float('inf')
maxi = float('-inf')
avg = 0
n = 0
line = data.readline()
while len(line) > 0:
    sid,val = line.split()
    val = float(val)
    if sid[:2] == query[-2:]:
        mini = min(val,mini)
        maxi = max(val,maxi)
        avg += val
        n += 1
    line = data.readline()
data.close()
if n == 0:
    print("No data")
else:
    avg /= n
    print(mini,maxi,avg)

