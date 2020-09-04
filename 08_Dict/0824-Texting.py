t2k = {
    " ":"0",
    "a":"2", "b":"22", "c":"222",   
    "d":"3", "e":"33", "f":"333",
    "g":"4", "h":"44", "i":"444",
    "j":"5", "k":"55", "l":"555",
    "m":"6", "n":"66", "o":"666",
    "p":"7", "q":"77", "r":"777", "s":"7777",
    "t":"8", "u":"88", "v":"888",
    "w":"9", "x":"99", "y":"999", "z":"9999"
}
k2t = {}
for key in t2k:
    k2t[t2k[key]] = key

def cleartext(text):
    text = text.lower()
    use = ""
    for c in text:
        if c in "abcdefghijklmnopqrstuvwxyz ":
            use += c
    return use

def text2keys(text):
    text = cleartext(text)
    keys = []
    for c in text:
        keys.append(t2k[c])
    return " ".join(keys)

def keys2text(keys):
    keys = keys.split()
    text = ""
    for k in keys:
        text += k2t[k]
    return text

exec(input().strip())
