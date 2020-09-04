class roman:
    def __init__(self,r):
        v = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        self.r = r
        self.val = 0
        for i in range(len(r)):
            self.val += v[r[i]]
            if i>0 and v[r[i]] > v[r[i-1]]:
                self.val -= 2*v[r[i-1]]

    def toRoman(n):
        r = ""
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        sym = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        i = 0
        while n>0:
            for j in range(n//val[i]):
                r += sym[i]
                n -= val[i]
            i += 1
        return r

    def __lt__(self,rhs):
        return self.val < rhs.val

    def __str__(self):
        return self.r
    
    def __int__(self):
        return self.val

    def __add__(self,rhs):
        return roman(roman.toRoman(self.val + rhs.val))

t, r1, r2 = input().split() 
a = roman(r1); b = roman(r2) 
if t == '1' : print(a < b) 
elif t == '2' : print(int(a),int(b)) 
elif t == '3' : print(str(a),str(b)) 
elif t == '4' : print(int(a + b)) 
else : print(str(a + b))