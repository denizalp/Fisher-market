import numpy as np
import economy as e

# Note, we assume that each firm produces one good, hence |goods|  = |firms|

# Matrix of valuations of buyers/workers: |buyers| x |goods|
demandV = np.array([[1,3,5,1,2], [2,5,6,2,6], [6,3,5,1,4], [3,3,4,2,6]])

# Matrix of valuations of firms: |firms| x |workers|
supplyV = np.array([[4,3,2,1], [1,5,4,2], [6,3,2,3], [2,5,3,2], [1,5,7,2]])

# Budgets of firms: |buyers|
supplyB = np.array([20, 23, 54, 12, 36])

# Create Market
market1 = e.Economy(supplyV, supplyB, demandV)

# Check if the iterative process converges
market1.solve(0.001)
