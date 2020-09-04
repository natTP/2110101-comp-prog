w = input()

if w[-1] in "sx" or w[-2:] == "ch":
    w += "es"
elif w[-1] == "y" and w[-2] not in "aeiou":
    w = w[:-1] + "ies"
else:
    w += "s"
print(w)