import numpy as np
import cvxpy as cp

def cell_solver(X,b,p):
    B=np.diag(b)
    Y=X @ B
    D=X.shape[0]
    
    # CVX solver starts here
    qcp=cp.Variable(D) # Create a vector variable.
    cost=cp.sum(cp.power(Y.T @ qcp,p))
    constraints = [cp.norm(qcp) <= 1]
    prob = cp.Problem(cp.Maximize(cost), constraints)
    prob.solve()
    q = qcp.value
    metric = prob.value
    
    return q, metric 
