bids = {} # obj:{person:(price,order)}
bidders = set()

#collect all bids
n = int(input())
for order in range(n):
    inp = input().split()
    if inp[0] == 'B':
        person, obj, price = inp[1:]; price = int(price)
        bidders.add(person)
        if obj not in bids:
            bids[obj] = {}
        bids[obj][person] = (price,order)
    elif inp[0] == 'W':
        person, obj = inp[1:]
        if (obj in bids) and (person in bids[obj]):
            bids[obj][person] = (0,order)

#who gets what
ans = {}
for p in bidders:
    ans[p] = []
for obj in bids:
    maxprice,_,maxbidder = max([(price,-order,person) for person,(price,order) in bids[obj].items()])
    if maxprice > 0:
        ans[maxbidder].append((maxprice,obj))
        
#print results
for p in sorted(bidders):
    price = sum([v for (v,o) in ans[p]])
    obj = sorted([o for (v,o) in ans[p]])
    if len(obj) == 0:
        print(p+": $0")
    else:
        print(p+": $"+str(price),"->"," ".join(obj))