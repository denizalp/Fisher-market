#%%
import numpy as np
import economy as e


# Note, we assume that each firm produces one good, hence |goods|  = |firms|
# Furthermore since every worker is also a buyer |buyer| = |workers|

############################### Example 1 ######################################

# Matrix of valuations of buyers/workers: |buyers| x |goods|
demandV = np.array([[1,3,5,1,2], [2,5,6,2,6], [6,3,5,1,4], [3,3,4,2,6]])

# Matrix of valuations of firms: |firms| x |workers|
supplyV = np.array([[4,3,2,1], [1,5,4,2], [6,3,2,3], [2,5,3,2], [1,5,7,2]])

# Budgets of firms: |buyers|
supplyB = np.array([20, 23, 54, 12, 36])

# Create Market
market1 = e.Economy(supplyV, supplyB, demandV)

#### Check if the iterative process converges
# Linear Utilities
Q, p, X, w, B = market1.solve(0.001, supplyB, "linear", "linear", printResults = True) # Converges

# Quasilinear Utilities
Q, p, X, w, B = market1.solve(0.001, supplyB, "linear", "linear", printResults = True) # For this one definitely contraction




############ Example 2 ############
# |buyers| = |workers| = 4
# |goods|  = |jobs| = 2

# Matrix of valuations of buyers/workers: |buyers| x |goods|
demandV = np.array([[10,34], [24,23], [0,50], [12,44]])

# Matrix of valuations of firms: |firms| x |workers|
supplyV = np.array([[4, 3, 5 ,0], [0, 5, 4, 7]])

# Budgets of firms: |buyers|
supplyB = np.array([151, 256])

# Create Market
market1 = e.Economy(supplyV, supplyB, demandV)

##### Check if the iterative process converges

# Linear Utilities
Q, p, X, w, B = market1.solve(0.001, supplyB, "linear", "linear", printResults = True) # For this one definitely contraction

# Quasilinear Utilities
Q, p, X, w, B = market1.solve(0.001, supplyB, "quasi-linear", "linear", printResults = True) # For this one definitely contraction



############ Example 3: Not contraction (because goods are not good?) ############

# Matrix of valuations of buyers/workers: |buyers| x |goods|
demandV = np.array([[0,10], [10,0], [0,10], [10,0]])

# Matrix of valuations of firms: |firms| x |workers|
supplyV = np.array([[10, 0, 10 ,0], [0, 10, 0, 10]])

# Budgets of firms: |buyers|
supplyB = np.array([150, 250])

# Create Market
market1 = e.Economy(supplyV, supplyB, demandV)

#### Check if the iterative process converges

# Linear Utilities
Q, p, X, w, B = market1.solve(0.001, supplyB, "linear", "linear", printResults = True) # For this one definitely contraction

# Quasilinear Utilities
Q, p, X, w, B = market1.solve(0.001, supplyB, "quasi-linear", "quasi-linear", printResults = True) # For this one definitely contraction


#%%
############ Example 4 ############

# Matrix of valuations of buyers/workers: |buyers| x |goods|
demandV = np.array([[10, 2], [2, 10]])

# Matrix of valuations of firms: |firms| x |workers|
supplyV = np.array([[5, 10], [10, 5]])

# Budgets of firms: |buyers|
supplyB = np.array([0.7, 0.3])



# Create Market
market1 = e.Economy(supplyV, supplyB, demandV)

#### Check if the iterative process converges

# Linear Utilities
Q, p, X, w, B = market1.solve(0.001, supplyB, "leontief", "leontief", printResults = True) # For this one definitely contraction

# # Quasilinear Utilities
# Q, p, X, w, B = market1.solve(0.001, supplyB, "quasi-linear", "quasi-linear", printResults = True) # For this one definitely contraction


# %%
