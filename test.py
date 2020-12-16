import numpy as np
from exhaustive_search_solver import *
# D: number of rows (features)
# N: nimber of columns (data measuremnts)
D,N=3,6

p=1/2
X=np.random.randn(D,N)
q, metric = exhaustive_search_solver(X , p)

print(q)
print(metric)
