import numpy as np
import algorithm as lppc
D = 3
N = 5
p = 1/2
X = np.random.randn(D, N)
qopt, bopt, metopt = lppc.exact_exhaustive(X, p)
