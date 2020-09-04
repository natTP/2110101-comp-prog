y = [float(e) for e in input().split()]
peaks = 0
#if y[0] > y[1]:
#    peaks += 1
for i in range(1,len(y)-1):
    if y[i]> y[i-1] and y[i]>y[i+1]:
        peaks += 1
#if y[-1]> 
print(peaks)