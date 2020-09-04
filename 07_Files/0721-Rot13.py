def rot13(t):
    encoded = ""
    upperc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerc = upperc.lower()
    for c in t:
        if "A" <= c <= "Z":
            encoded += upperc[(upperc.index(c)+13)%26]
        elif "a" <= c <= "z":
            encoded += lowerc[(lowerc.index(c)+13)%26]
        else:
            encoded += c
    return encoded

inp = input()
while inp != "end":
    print(rot13(inp))
    inp = input()