import numpy as np
import cvxpy as cp
import math
import cvxopt 

def LpPC_exact_exhaustive(X , p, verbose=0):
    D, N = X.shape[0], X.shape[1]
    B = bin_array_2D(N)
    b=B[0,:]
    q_best, metric_best, solved_status=cell_solver(X,b,p,verbose)

    cells_solved=0
    cells_nonsolved=0


    if solved_status:
        cells_solved+=1
    else:
        cells_nonsolved+=1

    for n in range(B.shape[0]-1):
        b=B[n+1,:]
        q,metric,solved_status=cell_solver(X,b,p,verbose)

        if solved_status:
            cells_solved+=1
        else:
            cells_nonsolved+=1

        if metric>metric_best:
            q_best=q
            metric_best=metric

    

    exp_num=0
    for i in range(D):
        exp_num+=math.comb(N-1, i)
    exp_num=exp_num*2

    if verbose >= 1:
        print("-----------------------------------")
        print("Number of candidate cells examined: " + str(2**N) )
        print("Number of cells with solution: " + str(cells_solved) )
        print("Number of cells with no solution: " + str(cells_nonsolved) )
        print("Expected number of cells with solution: " + str(exp_num) )
        print("Norm of best q: " + str(np.sqrt(q_best.T @ q_best)) )
        print("Optimal metric: " + str(metric_best))

    return q_best, metric_best, cells_solved, cells_nonsolved


def bin_array_1D(num, m):
    #Convert a positive integer num into an m-bit bit vector
    return np.array(list(np.binary_repr(num).zfill(m))).astype(np.int8)

def bin_array_2D(N):    
    L=2**N
    B=np.zeros((L,N))
    for n in range(L):
        B[n:,:]=bin_array_1D(n, N)
    return 2*B-1

def cell_solver(X,b,p, verbose=0):
    # print(cp.installed_solvers())
    B=np.diag(b)
    Y=X @ B
    D=X.shape[0]
    
    # CVX solver starts here
    qcp=cp.Variable(D) # Create a vector variable.
    cost=cp.sum(cp.power(Y.T @ qcp,p))
    constraints = [cp.norm(qcp) <= 1, Y.T @ qcp >=0 ]
    prob = cp.Problem(cp.Maximize(cost), constraints)
    try:
        prob.solve(solver = 'CVXOPT' , verbose = False)
        q = qcp.value
        metric = prob.value
        solved_status=True
    except:
        if verbose==2:
            print('Infeasible (empty) cell suspected')
            print('Cell id: ' + str(b))
        q = np.zeros(D)
        solved_status=False
        metric = 0
    
    
    return q, metric ,solved_status
