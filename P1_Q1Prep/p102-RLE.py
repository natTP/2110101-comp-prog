instruction = input()

if instruction == "str2RLE":
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
elif instruction == "RLE2str":
    inp = input().split()
    decode = ""
    for i in range(0,len(inp),2):
        decode += inp[i]*int(inp[i+1])
    print(decode)
else:
    print("Error")