inp = input()
sales = inp.split()

total = 0
for i in range(7):
    total += int(sales[i])
print(total)