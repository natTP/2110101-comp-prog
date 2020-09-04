class Card: 

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "(" + str(self.value) + " " + str(self.suit) + ")"

    def next1(self):
        v = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        s = ["club","diamond","heart","spade"]
        i = v.index(self.value)
        if self.suit == "spade":
            newsuit = "club"
            newval = v[(i+1)%13]
        else:
            j = s.index(self.suit)
            newsuit = s[(j+1)%4]
            newval = self.value
        return Card(newval,newsuit)

    def next2(self):
        v = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        s = ["club","diamond","heart","spade"]
        i = v.index(self.value)
        if self.suit == "spade":
            self.suit = "club"
            self.value = v[(i+1)%13]
        else:
            j = s.index(self.suit)
            self.suit = s[(j+1)%4]

n = int(input()) 
cards = [] 
for i in range(n): 
    value, suit = input().split() 
    cards.append(Card(value, suit)) 
for i in range(n):
    print(cards[i].next1()) 
print("----------") 
for i in range(n): 
    print(cards[i]) 
print("----------") 
for i in range(n): 
    cards[i].next2() 
    cards[i].next2() 
    print(cards[i])