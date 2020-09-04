docs = {}
n = int(input())
for k in range(n):
    name = input()
    inp = input().split()
    docs[name] = {}
    for word in inp:
        if word in docs[name]:
            docs[name][word] += 1
        else:
            docs[name][word] = 1

inp = input()
while inp != "-1":
    found = False
    score = 0
    maxscore = 0
    maxdoc = ""
    for doc in docs:
        allw = 0
        for word in docs[doc]:
            allw += docs[doc][word]
        if inp in docs[doc]:
            score = (docs[doc][inp]/allw) / len(docs[doc])
        if score > maxscore:
            maxscore = score
            maxdoc = doc
    if maxscore == 0:
        print("NOT FOUND")
    else:
        print(maxdoc)
    inp = input()

#27 min approx after minus playing around