n = int(input())
val = [n]
while n != 1:
    if n%2 == 0:
        n //= 2
        val.append(n)
    else:
        n = 3*n + 1
        val.append(n)
out = ""
for num in val[-15:]:
    out += str(num) + "->"
print(out[:-2])