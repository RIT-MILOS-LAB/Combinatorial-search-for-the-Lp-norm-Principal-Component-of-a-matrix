from LpPC_exact_exhaustive import *

D=3
N=8

p=1/2
X=np.random.randn(D,N)
q, metric, cells_solved, cells_nonsolved = LpPC_exact_exhaustive(X , p, verbose=1)
