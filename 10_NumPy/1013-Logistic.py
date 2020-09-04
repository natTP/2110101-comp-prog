import numpy as np

def p( X ):
    return 1/(1 + np.e ** (3.98 - 0.5*X[::,1:] - 0.1*X[::,:1]) ).reshape((X.shape[0]))

exec(input().strip())