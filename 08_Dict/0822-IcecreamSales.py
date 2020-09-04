n = int(input())
icecream = {}
for k in range(n):
    name,price = input().split()
    icecream[name] = float(price)

m = int(input())
sales = {}
maxsale = -1.0
totsale = 0.0
for k in range(m):
    product,amount = input().split()
    if product in icecream:
        thissale = icecream[product]*(float(amount))
        totsale += thissale
        if product not in sales:
            sales[product] = thissale
        else:
            sales[product] += thissale
        if sales[product] > maxsale:
            maxsale = sales[product]
topice = []
for product in sales:
    if sales[product] == maxsale:
        topice.append(product)
topice.sort()
if maxsale == -1.0:
    print("No ice cream sales")
else:
    print("Total ice cream sales:",totsale)
    print("Top sales:",", ".join(topice))