star = {}
n = int(input())
for k in range(n):
    movie, name1, name2 = input().split(",")
    movie = movie.strip(); name1 = name1.strip(); name2 = name2.strip()
    if name1 in star:
        star[name1].append(movie)
    else:
        star[name1] = [ movie ]
    if name2 in star:
        star[name2].append(movie)
    else:
        star[name2] = [ movie ]
        
query = [ e.strip() for e in input().split(",") ]
for q in query:
    if q in star:
        print(q,"->",", ".join(star[q]))
    else:
        print(q,"-> Not found")
#11 min