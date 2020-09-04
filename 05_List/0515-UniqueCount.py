inp = [int(e) for e in input().split()]
inp.sort()
nums = [inp[0]]
cnt = 0
for i in range(0,len(inp)-1):
    if inp[i] != inp[i+1]:
        cnt += 1
        nums.append(inp[i+1])
nums.sort()
print(cnt + 1)
print(nums[:10])
