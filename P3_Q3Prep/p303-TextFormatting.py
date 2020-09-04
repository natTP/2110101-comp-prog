fname = input().strip()

k = int(input())
ruler = ""
for i in range(k//10):
    ruler += '-'*9 + str(i+1)
if k%10 != 0:
    ruler += '-'*(k%10)
print(ruler)

file = open(fname,"r+")
doc = ""
for line in file:
    doc += line.strip() + '.'
file.close()

while len(doc) > k:
    for i in range(k,-1,-1):
        if doc[i] == '.':
            break
        else:
            doc += '.'
            i = doc.find('.')
    print(doc[:i].strip('.'))
    doc = doc[i:].strip('.')
if len(doc)>0:
    print(doc.strip('.'))