m = input()
n = int(input())

l = len(m)
if(l<n):
    m = "0"*(n-l) + m

print(m)