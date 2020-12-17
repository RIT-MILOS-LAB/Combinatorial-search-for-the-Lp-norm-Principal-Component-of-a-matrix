from LpPC_exact_exhaustive import *

D=3
N=10

p=1/10
X=np.random.randn(D,N)
q, metric, cells_solved, cells_nonsolved = LpPC_exact_exhaustive(X , p, verbose=1)
