def graycode(n):
    code = ['0','1']
    for i in range(n-1):
        codeL = list(code)
        codeR = codeL[-1::-1]
        for i in range(len(codeL)):
            codeL[i] = '0' + codeL[i]
        for i in range(len(codeR)):
            codeR[i] = '1' + codeR[i]
        code = codeL + codeR
    return code

#OR t = ['0','1']
#for i in range(n-1): t = ['0'+e for r in t] + ['1'+e for e in t[::-1]] 

n = int(input())
k = int(input())

valid = True

if (n <= 0 or int(n) != n) and (k<1):
    print("Invalid n and k")
    valid = False
elif n <= 0 or int(n) != n:
    print("Invalid n")
    valid = False
elif k<1:
    print("Invalid k")
    valid = False

if valid:
    out = ""
    for i in range(1,k+1):
        m = n+1
        if i == k:
            m = n
        m -= len(str(i))
        out += str(i) + '-'*m
    print(out)
    
    done = False
    ans = graycode(n)
    index = 0
    for i in range(len(ans)//k + 1):
        out = ""
        for j in range(k):
            out += ans[index] + ","
            index += 1
            if index == len(ans):
                done = True
                break
        print(out[:-1])
        if done:
            break
        
#44-- min with interruptions n sleepiness, 3 subs