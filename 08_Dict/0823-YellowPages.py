n = int(input())
name = {}
number = {}
for k in range(n):
    firstname,surname,num = input().split()
    person = firstname + " " + surname
    name[person] = num
    number[num] = person

m = int(input())
for i in range(m):
    q = input()
    if q in name:
        print(q,"-->",name[q])
    elif q in number:
        print(q,"-->",number[q])
    else:
        print(q,"-->","Not found")