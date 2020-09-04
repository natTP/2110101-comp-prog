import math

ttlstroke = 0
ttlimpstroke = 0
ttlpar = 0

for i in range(9):
    par,stroke,chosen = [int(inp) for inp in input().split()]
    if chosen:
        ttlimpstroke += min(stroke,par+2)
    ttlpar += par
    ttlstroke += stroke
handi = math.floor((ttlimpstroke*1.5 - ttlpar)*0.8)

print(ttlstroke)
print(handi)
print(ttlstroke - handi)