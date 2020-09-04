inp1 = input()
inp2 = input()
 
inp1 = inp1[1:-1] 
inp2 = inp2[1:-1] 
v1 = inp1.split(",")
v2 = inp2.split(",")

add = [0.0,0.0,0.0]
for i in range(3):
    v1[i] = float(v1[i])
    v2[i] = float(v2[i])
    add[i] = v1[i] + v2[i]

print(v1,"+",v2,"=",add)