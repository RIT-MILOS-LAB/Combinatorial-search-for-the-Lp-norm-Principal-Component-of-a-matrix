import numpy as np
import cvxpy as cp
import cvxopt 

def cell_solver(X,b,p):
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
    except:
        print('Infeasible (empty) cell suspected')
        print('Cell id: ' + str(b))
        q = np.zeros(D)
        metric = 0
    
    
    return q, metric 
