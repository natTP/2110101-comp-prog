q = []
qnum = 1
totalT = 0
customers = 0
qToOrder = 0
n = int(input())
for k in range(n):
    inp = input().split()
    if inp[0] == 'reset':
        qnum = int(inp[1])
    elif inp[0] == 'new':
        q.append([qnum,int(inp[1])]) # [queue, init_time]
        print("ticket",qnum)
        qnum += 1
    elif inp[0] == 'next':
        print("call",q[0][0])
        qToOrder = q[0]
        q.pop(0)
    elif inp[0] == 'order':
        qtime = int(inp[1])-qToOrder[1]
        print("qtime",qToOrder[0],qtime)
        customers += 1
        totalT += qtime
    elif inp[0] == 'avg_qtime':
        print("avg_qtime",round(totalT/customers,4))