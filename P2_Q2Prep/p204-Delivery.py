month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def isLeap(y):
    y -= 543
    return y%400 == 0 or (y%4 == 0 and y%100 != 0)

def shift(shifted,order):
    d,m,y = order[2:]
    if int(d) + shifted <= month[int(m)]:
        d = str(int(d) + shifted)
        return "/".join([d,m,y])
    d = str((int(d) + shifted) % month[int(m)])
    if int(m) == 12:
        y = str(int(y) + 1)
        m = '1'
    else:
        m = str(int(m) + 1)
    return "/".join([d,m,y])

def delivery(order):
    date = ""
    if order[1] == "E":
        date = shift(1,order)
    elif order[1] == "Q":
        date = shift(3,order)
    elif order[1] == "N":
        date = shift(7,order)
    elif order[1] == "F":
        date = shift(14,order)
    return date

def invalidDate(order):
    d,m,y = [int(c) for c in order[2:]]
    if d < 1:
        return True
    if m != 2:
        if d > month[m]:
            return True
        return False
    if isLeap(y):
        if d > 29:
            return True
        return False
    if d > month[m]:
        return True
    return False

error = []
correct = []

inp = input()
while inp != "END":
    order = inp.split()
    if int(order[4]) < 2558:
        error.append("Error: " + " ".join(order) + " --> Invalid year")
    elif 1 > int(order[3]) or int(order[3]) > 12:
        error.append("Error: " + " ".join(order) + " --> Invalid month")     
    elif invalidDate(order):
        error.append("Error: " + " ".join(order) + " --> Invalid date")    
    elif order[1] not in "EQNF":
        error.append("Error: " + " ".join(order) + " --> Invalid delivery type")
    else:
        ans = order[0] + ": delivered on "
        correct.append([[int(c) for c in delivery(order).split("/")[-1::-1]],ans + delivery(order)])
    inp = input()
correct.sort()

for s in error:
    print(s)
for s in correct:
    print(s[1])
    
#45 + 24 min with many interuptions