"""
Combinatorial search for the Lp-norm (p< = 1) Principal component of a matrix.
"""
__author__ = 'D. G. Chachlakis'
__email__ = 'dimitris@mail.rit.edu'
import numpy as np
from utils import *
def exact_exhaustive(X, p):
    """
    Input: 
    -------
    X: data matrix of size D-by-N: N D-dimensional measurements
    p: Lp-norm parameter,  p should be less than or equal to 1

    Output:
    -------
    qopt: an optimal Lp-PC of X
    bopt: an optimal antipodal binary vectror
    metopt: the maximum attainable metric
    """
    D = X.shape[0]
    N = X.shape[1]
    B = decimal2binary(list(range(2**N)), N)
    bopt = B[:, 0]
    qopt, metopt = solver_fixedb(X, bopt, p)
    for n in range(B.shape[1] - 1):
        b = B[:, n+1]
        q, met = solver_fixedb(X, b, p)
        if met > metopt:
            qopt = q
            bopt = b
            metopt = met
    print("\n=======================================")
    print("Number of candidates examined:\t"+str(2**N))
    print("Optimal metric:\t\t\t "+str(np.round(metopt, 4)))
    print("\n=======================================")
    return qopt, bopt, metopt