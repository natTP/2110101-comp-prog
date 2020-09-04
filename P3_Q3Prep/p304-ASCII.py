fname = input().strip()
q = input().strip()

data = open(fname)
left = right = 9999999
for line in data:
    line  = line.strip()
    for l in range(len(line)):
        if line[l] != '.':
            left = min(left,l)
            break
    for r in range(len(line)):
        if line[-(r+1)] != '.':
            right = min(right,r)
            break
data.close()

if q == "STRIP_ALL":
    lines = ""
    n = 0
    data = open(fname)
    for line in data:
        line = line.strip()
        line = line[left:len(line)-right]
        width = len(line)
        lines += line
        n += 1
    data.close()
    j = 0 #row i, column j
    while j < width:
        blank = True
        for i in range(0,n*width,width):
            if lines[j+i] != '.': #column not blank!
                blank = False
                j += 1
                break
        if blank: #remove
            t = ""
            for i in range(0,n*width,width):
                t += lines[i:i+j] + lines[i+j+1:i+width]
            lines = t
            width -= 1
    for i in range(n):
        print(lines[i*width:(i+1)*width])
    
elif q in ["LSTRIP","RSTRIP","STRIP"]:
    data = open(fname)
    if q == "LSTRIP":
        right = 0
    elif q == "RSTRIP":
        left = 0
    for line in data:
        line = line.strip()
        print(line[left:len(line)-right])
    data.close()
else:
    print("Invalid command")