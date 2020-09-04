target = input()
s = input() 
remove = ['"',"(",")",",",".","'"]

sentence = ""
for ch in s:
    if ch not in remove:
        sentence += ch
    else:
        sentence += " "
sentence = sentence.split()

cnt = 0
for word in sentence:
    if word == target:
        cnt += 1
print(cnt)
