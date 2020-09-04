n = int(input())
nickname = {}
realname = {}
for k in range(n):
    real,nick = input().split()
    realname[real] = nick
    nickname[nick] = real

m = int(input())
for k in range(m):
    name = input()
    if name in nickname: 
        print(nickname[name])
    elif name in realname:
        print(realname[name])
    else:
        print("Not found")