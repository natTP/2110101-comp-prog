n = int(input())
listt = []
i = 0
for k in range(n):
    inp = int(input())
    if i%2 == 0:
        listt.append(inp)
    else:
        listt.insert(0,inp)
    i += 1
inp = input()
for data in inp.split():
    data = int(data)
    if i%2 == 0:
        listt.append(data)
    else:
        listt.insert(0,data)
    i += 1
while True:
    inp = int(input())
    if inp == -1:
        break
    if i%2 == 0:
        listt.append(inp)
    else:
        listt.insert(0,inp)
    i += 1
print(listt)