cards = input().split()
instructions = input()
n = len(cards)

for inst in instructions:
    if inst == 'C': #cut
        for i in range(n//2):
            temp = cards[0]
            cards.pop(0)
            cards.append(temp)
    elif inst == 'S': #shuffle
        j = 0
        for i in range(n//2,n):
            temp = cards[i]
            cards.remove(temp)
            cards.insert(2*j+1,temp)
            j += 1
print(" ".join(cards))