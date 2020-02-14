import numpy as np
import cvxpy as cp
import fisherMarket as m
import fisherVerifer as fv
###### Market Parameters ######


############################### Example 1 ######################################

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1,3,5,1,2], [2,5,6,2,6], [6,3,5,1,4], [3,3,4,2,6]])

# Budgets of buyers: |buyers|
budgets = np.array([20, 23, 54, 12])

# Vector with quantity of goods: |goods|
numGoodsVec = np.array([1,2,6,4,3])

# Create Market
market1 = m.FisherMarket(valuations, budgets)

# Solve for market prices and allocations for desired utility function structure.

# Current Options are 'quasi-linear' and 'linear'
market1.solveMarket("quasi-linear")

X, p = market1.solveMarket("linear")

fv.verify(X, p, valuations, budgets, utility = "linear")

# Get demand and supply for each good (in dollar)
market1.getDS("quasi-linear")



############################### Example 2 ######################################

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1, 1, 1], [1, 1, 1]])

# Budgets of buyers: |buyers|

budgets = np.array([5, 5])

# Create Market
market1 = m.FisherMarket(valuations, budgets)

# Solve for market prices and allocations for desired utility function structure.

# Current Options are 'quasi-linear' and 'linear'
X, p = market1.solveMarket("linear")
# fv.verify(X, p, valuations, budgets, utility = "linear")


X, p = market1.solveMarket("quasi-linear")
# fv.verify(X, p, valuations, budgets, utility = "quasi-linear")
