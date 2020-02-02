import numpy as np
import cvxpy as cp
import market as m
###### Market Parameters ######


# Number of buyers in the market (row)
numberOfBuyers = 4

# Number of goods in the market (column)
numberOfGoods = 5

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1,3,5,1,2], [2,5,6,2,6], [6,3,5,1,4], [3,3,4,2,6]])

# Budgets of buyers: |buyers|
budgets = np.array([20, 23, 54, 12])

# Vector with quantity of goods: |goods|
numGoodsVec = np.array([1,2,6,4,3])

market1 = m.Market(valuations, budgets, numGoodsVec)

market1.getValuations()
market1.numberOfBuyers()
market1.numberOfGoods()
market1.solveMarket("quasi-linear")
market1.solveMarket("linear")
