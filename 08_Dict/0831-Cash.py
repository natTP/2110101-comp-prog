def total(pocket):
    tot = 0
    for bill in pocket:
        tot += bill*pocket[bill]
    return tot

def take(pocket,money):
    for bill in money:
        if bill in pocket:
            pocket[bill] += money[bill]
        else:
            pocket[bill] = money[bill]
    return pocket

def pay(pocket,amt):
    original = {}
    for key in pocket:
        original[key] = pocket[key]
    pay = {}
    if total(pocket) < amt:
        return {}
    for bill in [1000,500,100,50,20,10,5,1]:
        if bill in pocket:
            if amt//bill != 0:
                if bill == 1 and amt > pocket[1]:
                    for key in pocket:
                        pocket[key] = original[key]
                    return {}
                paidbills = min(amt//bill,pocket[bill])
                pocket[bill] -= paidbills
                pay[bill] = paidbills
                amt -= bill*paidbills
    if amt == 0:
        return pay
    for key in pocket:
        pocket[key] = original[key]
    return {} 

exec(input().strip())