inp = input()
previous = inp[0]
encode = str(inp[0]) + " "
cnt = 1
for ch in inp[1:]:
    if ch != previous:
        encode += str(cnt) + " "
        encode += ch + " "
        cnt = 1
    else:
        cnt += 1
    previous = ch
encode += str(cnt)
print(encode)