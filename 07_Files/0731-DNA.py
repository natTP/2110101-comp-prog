dna = input().strip().upper()
q = input()

valid = True
for c in dna:
    if c not in "ATCG":
        print("Invalid DNA")
        valid = False
        break

if valid:
    if q == 'R':
        r_dna = ""
        for c in dna:
            if c == 'A':
                r_dna += 'T'
            elif c == 'T':
                r_dna += 'A'
            elif c == 'G':
                r_dna += 'C'
            elif c == 'C':
                r_dna += 'G'
        print(r_dna[-1::-1])
    elif q == 'F':
        print("A=" + str(dna.count('A')) + ", T=" + str(dna.count('T')) + ", G=" + str(dna.count('G')) + ", C=" + str(dna.count('C')))
    elif q == 'D':
        want = input().upper()
        cnt = 0
        for i in range(len(dna)-1):
            if dna[i:i+2] == want:
                cnt += 1
        print(cnt)
