def camelCase(s):
    camel = ""
    firstL = True
    for i in range(len(s)):
        if 'A' <= s[i] <= 'z':
            if firstL:
                camel += s[i].lower()
                firstL = False
            else:
                if s[i-1] in " .()":
                    camel += s[i].upper()
                else:
                    camel += s[i].lower()
        if '0' <= s[i] <= '9':
            camel += s[i]
        else:
            camel += ""
    return camel

inp = input()
print(camelCase(inp))