import numpy as np

def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight,data):
    scoresum = np.sum(weight * data[:,1:],axis=1)
    mean = np.mean(scoresum)
    ans = list(str(a) for a in data[ scoresum < mean , 0])
    #ans = IDs[scoresum < mean] #IDS from 0th column
    if len(ans) == 0:
        print("None")
    else:
        print(", ".join(ans))

exec(input().strip())