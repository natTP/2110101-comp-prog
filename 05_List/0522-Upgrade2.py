inp = input()
students = []
possibleGrades = ["F","D","D+","C","C+","B","B+","A"]
while inp != "q":
    temp = inp.split()
    students.append([int(temp[0]),temp[1]])
    inp = input()
students.sort()
upgrades = [int(e) for e in input().split()]
for n in upgrades:
    indexN = 0
    grade = ""
    for i in range(len(students)):
        if students[i][0] == n:
            grade = students[i][1]
            indexN = i
    if grade != "A":
        students[indexN][1] = possibleGrades[possibleGrades.index(grade) + 1]
students.sort()

for i in range(len(students)):
    print(students[i][0],students[i][1])