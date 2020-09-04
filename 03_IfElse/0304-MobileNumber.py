n = input()

if len(n) != 10:
    print("Not a mobile number")
elif n[:2] == "06" or n[:2] == "08" or n[:2] == "09":
    print("Mobile number")
else:
    print("Not a mobile number")
