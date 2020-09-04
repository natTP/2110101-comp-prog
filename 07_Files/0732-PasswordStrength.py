pw = input()

good = True

#Rule 1
if len(pw) < 8:
    good = False
    print("Less than 8 characters")
hasLow = False 
hasUpp = False
hasNum = False
hasSym = False

#Rule2
for c in pw:
    if c in "abcdefghijklmnopqrstuvwxyz":
        hasLow = True
    elif c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        hasUpp = True
    elif c in "0123456789":
        hasNum = True
    elif c in "!@#$%^&*()_+-=[];:\'\"|/?<>,.":
        hasSym = True
if not hasLow:
    good = False
    print("No lowercase letters")
if not hasUpp:
    good = False
    print("No uppercase letters")
if not hasNum:
    good = False
    print("No numbers")
if not hasSym:
    good = False
    print("No symbols")

#Rule3
for i in range(len(pw)-3):
    if pw[i] == pw[i+1] == pw[i+2] == pw[i+3]:
        good = False
        print("Character repetition")
        break

#Rule4
for i in range(len(pw)-3):
    if pw[i:i+4] in "01234567890 09876543210":
        good = False
        print("Number sequence")
        break

#Rule5
for i in range(len(pw)-3):
    if pw[i:i+4].lower() in "abcdefghijklmnopqrstuvwxyz zyxwvutsrqponmlkjihgfedcba":
        good = False
        print("Letter sequence")
        break

#Rule6
for i in range(len(pw)-3):
    if pw[i:i+4].lower() in "!@#$%^&*()_+ +_)(*&^%$#@! qwertyuiop poiuytrewq asdfghjkl lkjhgfdsa zxcvbnm mnbvcxz":
        good = False
        print("Keyboard pattern")
        break

if good:
    print("OK")