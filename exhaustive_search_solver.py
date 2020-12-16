import numpy as np
from cell_solver import *

def exhaustive_search_solver(X , p):
    D, N = X.shape[0], X.shape[1]
    B = bin_array_2D(N)
    b=B[0,:]
    q_best, metric_best=cell_solver(X,b,p)
    for n in range(B.shape[0]-1):
        b=B[n+1,:]
        q,metric=cell_solver(X,b,p)
        if metric>metric_best:
            q_best=q
            metric_best=metric
    return q_best, metric_best


def bin_array_1D(num, m):
    #Convert a positive integer num into an m-bit bit vector
    return np.array(list(np.binary_repr(num).zfill(m))).astype(np.int8)

def bin_array_2D(N):    
    L=2**N
    B=np.zeros((L,N))
    for n in range(L):
        B[n:,:]=bin_array_1D(n, N)
    return 2*B-1


