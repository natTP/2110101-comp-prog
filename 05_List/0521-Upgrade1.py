inp = input()
stuIds = []
stuGrades = []
possibleGrades = ["F","D","D+","C","C+","B","B+","A"]
while inp != "q":
    temp = inp.split()
    stuIds.append(temp[0])
    stuGrades.append(temp[1])
    inp = input()
upgrades = [e for e in input().split()]
for n in upgrades:
    grade = stuGrades[stuIds.index(n)]
    if grade != "A":
        stuGrades[stuIds.index(n)] = possibleGrades[possibleGrades.index(grade) + 1]

for stu in stuIds:
    grade = stuGrades[stuIds.index(stu)]
    print(stu,grade)