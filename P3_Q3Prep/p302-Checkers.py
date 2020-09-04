pos = input().strip()

row = ""
col = ""
if len(pos) <= 3:
    row = pos[0]
    col = pos[1:]
else:
    i = pos.find("=",pos.find("row"))
    j = pos.find("=",pos.find("col"))
    k = pos.find(",")
    if i < k: #row comes first
        row = pos[i+1:k]
        col = pos[j+1:]
    else: #col comes first
        col = pos[j+1:k]
        row = pos[i+1:]

row = row.strip()
col = col.strip().lstrip("0")

rowvalid = True
colvalid = True
rowname = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

if row not in rowname or row == "":
    rowvalid = False
if col not in [ str(c) for c in range(1,53) ]:
    colvalid = False

if not rowvalid and not colvalid:
    print("Invalid row and column")
elif not rowvalid:
    print("Invalid row")
elif not colvalid:
    print("Invalid column")
else:
    r = rowname.find(row)
    if r%2 == int(col)%2:
        print("Black")
    else:
        print("White")
#67 min with google