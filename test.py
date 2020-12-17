import numpy as np
from exhaustive_search_solver import *
# D: number of rows (features)
# N: nimber of columns (data measuremnts)
print(20*'\n')
D,N=4,8

p=4/5
X=np.random.randn(D,N)
q, metric = exhaustive_search_solver(X , p)

print(q)
print(q.T @ q)
print(metric)
