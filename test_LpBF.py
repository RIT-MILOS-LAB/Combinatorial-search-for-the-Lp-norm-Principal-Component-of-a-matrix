from LpBF import *
import matplotlib.pyplot as plt

# Create a matrix of size D-by-N, D features, N columns
D=10
N=20
X=np.random.randn(D,N)

# Choose a p<=1 value
p=1/2

# Find the Lp-PC of X by calling LpBF
q, metric, metric_across_iter = LpBF( X , p , verbose=True)

# Plot the evolution of the metric across iterations
plt.plot(range(len(metric_across_iter)),metric_across_iter)
plt.ylabel('Lp-PCA metric')
plt.xlabel('Iteration index')
plt.show()
