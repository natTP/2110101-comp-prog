def is_prime(n):
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            return False
    return True

def next_prime(n):
    k = n+1
    while True:
        if is_prime(k):
            return k
        k += 1

def next_twin_prime(n):
    p1 = next_prime(n)
    while True:
        if is_prime(p1+2):
            return "(" + str(p1) + ", " + str(p1+2) + ")"
        p1 = next_prime(p1)

exec(input().strip())
