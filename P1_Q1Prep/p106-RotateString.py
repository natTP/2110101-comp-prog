instruction = input()
n = int(input())
string = ""
do = True
for i in range(n):
    inp = input().strip()
    if i == 0:
        linelen = len(inp)
    else:
        if len(inp) != linelen:
            print("Invalid size")
            do = False
            break
    string += inp

if do:
    i = 0
    if instruction == '90':
        while i < linelen:
            s = string[i::linelen]
            print(s[-1::-1])
            i += 1
    elif instruction == 'flip':
        while i <= len(string):
            s = string[i:i+linelen]
            print(s[-1::-1])
            i += linelen
    if instruction == '180':
        string = string[-1::-1]
        while i <= len(string):
            print(string[i:i+linelen])
            i += linelen
