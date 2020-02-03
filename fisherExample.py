import numpy as np
import cvxpy as cp
import fisherMarket as m
###### Market Parameters ######


# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1,3,5,1,2], [2,5,6,2,6], [6,3,5,1,4], [3,3,4,2,6]])

# Budgets of buyers: |buyers|
budgets = np.array([20, 23, 54, 12])

# Vector with quantity of goods: |goods|
numGoodsVec = np.array([1,2,6,4,3])

# Create Market
market1 = m.FisherMarket(valuations, budgets, numGoodsVec)

# Solve for market prices and allocations for desired utility function structure.

# Current Options are 'quasi-linear' and 'linear'
market1.solveMarket("quasi-linear")
market1.solveMarket("linear")
