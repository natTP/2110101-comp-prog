num = ["soon","neung","song","sam","si","ha","hok","chet","paet","kao","sip"]

def to_Thai(n):
    ans = ""
    if n <= 10:
        return num[n]
    if n >= 1000:
        c = n//1000
        ans += " " + num[c] + " pun"
        n %= 1000
    if n >= 100:
        c = n//100
        ans += " " + num[c] + " roi"
        n %= 100
    if n >= 10:
        c = n//10
        if c == 1:
            ans += " sip"
        elif c == 2:
            ans += " yi sip"
        else:
            ans += " " + num[c] + " sip"
        n %= 10
    if n == 1:
        ans += " et"
    elif n > 1:
        ans += " " + num[n]
    return ans

exec(input().strip())
#14 min