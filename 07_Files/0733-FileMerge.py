def read_next(f):
    while True:
        t = f.readline()
        if len(t) == 0: # ถ้าอ่านหมดแล้ว ออกจากวงวน
            break
        x = t.strip().split() # ลบ blank ซ้ายขวา
        if len(x) == 2: # แยกแล้วได้ 2 ส่วน --> ถูกต้อง ก็คืนผล
            return x[0], x[1]
    return "", "" # แฟ้มหมดแล้ว คืนสตริงว่าง

file1,file2 = input().split()

data1 = open(file1,"r")
data2 = open(file2,"r")

idA,gradeA = read_next(data1)
idB,gradeB = read_next(data2)
#print(idA,gradeA)
#print(idB+"yay"+gradeB+"yay")
readA = False
readB = False

while idA != "" or idB != "":
    if idA == "":
        print(idB,gradeB)
        readB = True
        readA = False
    elif idB == "":
        print(idA,gradeA)
        readA = True
        readB = False
    elif idA[-2:] == idB[-2:]:
        if idA < idB:
            print(idA,gradeA)
            readA = True
            readB = False
        else:
            print(idB,gradeB)
            readB = True
            readA = False
    elif idA[-2:] < idB[-2:]:
        print(idA,gradeA)
        readA = True
        readB = False
    elif idA[-2:] > idB[-2:]:
        print(idB,gradeB)
        readB = True
        readA = False

    if readA:
        idA,gradeA = read_next(data1)
    elif readB:
        idB,gradeB = read_next(data2)

data1.close()
data2.close()