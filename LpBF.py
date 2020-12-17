import numpy as np
import cvxpy as cp
import cvxopt

def LpBF(X, p, verbose=False):
    
    tol=1e-6
    D=X.shape[0]
    N=X.shape[1]
    q=np.random.randn(D,1)
    q=q/np.sqrt(q.T @ q)
    b_best=np.sign(X.T @ q).flatten()
    q_best, metric_best=cell_solver(X,b_best,p)

    metric_across_iter=[]
    metric_across_iter.append(metric_best)
    
    it=0
    if verbose:
        print('Iteration: ' + str(it) + ', Metric: ' + str(metric_best))

    I=np.eye(N)
    while True:
        val=np.zeros((N,1))
        for n in range(N):
            bn = b_best -2*b_best[n]*I[:,n]
            q, metric=cell_solver(X,bn,p)
            val[n]=metric
        met=np.max(val)
        idx=np.argmax(val)
        if met-metric_best>tol:
            metric_best=met
            b_best=b_best -2*b_best[idx]*I[:,idx]
            metric_across_iter.append(metric_best)
        else:
            break
        it+=1
        if verbose:
            print('Iteration: ' + str(it) + ', Metric: ' + str(metric_best))
    return q_best, metric_best, metric_across_iter


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
