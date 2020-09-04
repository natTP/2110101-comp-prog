inp = input()
notin = ""
for i in range(10):
    if str(i) not in inp:
        notin += str(i) + ","
if len(notin) == 0:
    print("None")
else:
    print(notin[:-1])
