c = input()

n = 0
for i in range(12):
    n += (13-i)*int(c[i])
check = (11 - n%11)%10

print(c[0:1] + " " + c[1:5] + " " + c[5:10] + " " + c[10:] + " ", check)
