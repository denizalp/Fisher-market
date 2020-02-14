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

# Check if the iterative process converges
market1.solve(0.001, "quasi-linear") # For this one definitely contraction
market1.solve(0.0001, "quasi-linear") # For this one definitely contraction



market1.solve(0.0001, "linear") # Converges

market1.solve(0.00001, "linear") # Bouncing around and not converging




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

# Check if the iterative process converges
market1.solve(0.0001, "quasi-linear") # For this one definitely contraction

market1.solve(0.00001, "quasi-linear") # For this one definitely contraction


market1.solve(0.0001, "linear") # For this one definitely contraction






############ Example 3: Not contraction (because goods are not good?) ############

# Matrix of valuations of buyers/workers: |buyers| x |goods|
demandV = np.array([[0,34], [24,0], [0,50], [12,0]])

# Matrix of valuations of firms: |firms| x |workers|
supplyV = np.array([[4, 0, 5 ,0], [0, 5, 0, 7]])

# Budgets of firms: |buyers|
supplyB = np.array([151, 256])



# Create Market
market1 = e.Economy(supplyV, supplyB, demandV)

# Check if the iterative process converges
market1.solve(0.0001, "quasi-linear") # For this one definitely contraction


market1.solve(0.0001, "linear") # For this one definitely contraction
