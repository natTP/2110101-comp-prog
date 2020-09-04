def read_date():
    mname = ["Jan", "Feb","Mar","Apr", "May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"] 
    date = input().split() 
    return [int(date[0]), mname.index(date[1][:3]) + 1, int(date[2])]

def zodiac(d1,m1):
    if d1 >= 22 and m1==3 or d1 <=21 and m1==4 : z1 = "Aries" 
    elif d1 >= 22 and m1==4 or d1 <=21 and m1==5 : z1 = "Taurus" 
    elif d1 >= 22 and m1==5 or d1 <=21 and m1==6 : z1 = "Gemini" 
    elif d1 >= 22 and m1==6 or d1 <=21 and m1==7 : z1 = "Cancer" 
    elif d1 >= 22 and m1==7 or d1 <=21 and m1==8 : z1 = "Leo" 
    elif d1 >= 22 and m1==8 or d1 <=21 and m1==9 : z1 = "Virgo" 
    elif d1 >= 22 and m1==9 or d1 <=21 and m1==10 : z1 = "Libra" 
    elif d1 >= 22 and m1==10 or d1 <=21 and m1==11 : z1 = "Scorpio" 
    elif d1 >= 22 and m1==11 or d1 <=21 and m1==12 : z1 = "Sagittarius" 
    elif d1 >= 22 and m1==12 or d1 <=20 and m1==1 : z1 = "Capricorn" 
    elif d1 >= 21 and m1==1 or d1 <=20 and m1==2 : z1 = "Aquarius" 
    elif d1 >= 21 and m1==2 or d1 <=21 and m1==3 : z1 = "Pisces"
    return z1

def days_in_feb(y):
    if y%400 == 0 or (y%4 == 0 and y%100 != 0):
        return 29
    return 28

def days_in_month(m,y):
    dinm = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if m == 2:
        return days_in_feb(y)
    return dinm[m]

def days_in_between(d1,m1,y1,d2,m2,y2):
    dinm = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    totd = 0
    if y1 == y2:
        dinm[2] = days_in_feb(y1)
        for i in range(m1+1,m2):
            totd += dinm[i]
        totd += d2 + (dinm[m1]-d1) - 1
    else:
        for y in range(y1+1,y2):
            totd += 337 + days_in_feb(y)
        #print(totd)
        dinm[2] = days_in_feb(y1)
        for i in range(m1+1,13):
            totd += dinm[i]
        totd += dinm[m1]-d1
        #print(totd)
        dinm[2] = days_in_feb(y2)
        for i in range(1,m2):
            totd += dinm[i]
        totd += d2 - 1
    return totd

def main(): 
    d1,m1,y1 = read_date() 
    d2,m2,y2 = read_date()
    print(zodiac(d1,m1),zodiac(d2,m2))
    print(days_in_between(d1,m1,y1,d2,m2,y2))

exec(input().strip())

