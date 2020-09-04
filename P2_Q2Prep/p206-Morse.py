file = input().strip()
data = open(file,"r")
q = data.readline()
pattern = data.readline()

if q == "T2M\n":
    for line in data:
        valid = True
        text = line.strip()
        morse = ""
        for e in text:
            if e in pattern:
                j = pattern.find('[' + e + ']')
                j += 3
                k = pattern.find('[',j)
                morse += pattern[j:k] + " "
            else:
                print("Invalid :",text)
                valid = False
                break
        if valid:
            print(morse)
    
elif q == "M2T\n":
    for line in data:
        valid = True
        morse = line.strip().split()
        text = ""
        for e in morse:
            e = ']' + e + '['
            if e in pattern:
                j = pattern.find(e)
                j -= 1
                text += pattern[j]
            else:
                print("Invalid :"," ".join(morse))
                valid = False
                break
        if valid:
            print(text)
        
else:
    print("Invalid code")
        
data.close()
#5+32 min WRONG IN PRINTING FORMAT