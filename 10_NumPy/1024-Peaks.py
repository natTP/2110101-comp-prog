import numpy as np

def peak_indexes(x):
    index = np.arange(x.shape[0]-1)
    return index[ (x[index] > x[index+1]) & (x[index] > x[index-1]) ]

def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")

exec(input().strip())