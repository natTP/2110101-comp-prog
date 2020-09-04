import math

def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

def is_coprime(a, b, c):
    return gcd(a, gcd(b,c)) == 1

def primitive_Pythagorean_triples(max_len):
    triple = []
    for i in range(3,max_len+1): #a
        for j in range(i,max_len+1): #b
            k = int(math.sqrt(i**2 + j**2))
            if k <= max_len and k**2 == i**2 + j**2 and is_coprime(i,j,k):
                triple.append([k,i,j])
    triple.sort()
    return [ [val[1],val[2],val[0]] for val in triple ]

exec(input().strip())