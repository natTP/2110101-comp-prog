inp = input()

letter = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

s1 = inp[3::7]
#print(s1)
s2 = inp[7::5]
#print(s2)
s3 = str(int(s1) + int(s2) + 10000)
#print(s3)
s4 = s3[-4:-1]
#print(s4)
temp = int(s4[0]) + int(s4[1]) + int(s4[2])
#print(temp)
n5 = temp%10 + 1
#print(n5)
l = letter[n5]

print(s4 + l)