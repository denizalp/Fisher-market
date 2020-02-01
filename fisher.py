import numpy as np
import cvxpy as cp

###### Market Parameters ######


# Number of goods in the market
numberOfGoods = 5

# Number of buyers in the market
numberOfBuyers = 4

# Vector with quantity of goods: |goods|
numGoodsVec = np.array([1,2,6,4,3])

# Matrix of valuations: |goods| x |buyers|
valuations = np.array([[1,3,5,1], [2,5,6,2], [6,3,5,1], [3,3,4,2], [2,6,4,6]])

# Budgets of buyers: |buyers|
budgets = np.array([20, 23, 54, 12])



####################
###### Solver ######
####################

#################################### CVXPY ####################################


####### Quasi-Linear Fisher Market #######

# Primal: Output => Prices
prices = cp.Variable(numberOfGoods)
betas = cp.Variable(numberOfBuyers)

obj = cp.Minimize(cp.sum(prices) - budgets.T @ cp.log(betas))

constraints = [prices >= valuations @ betas, betas <= 1]

problem = cp.Problem(obj, constraints)

problem.solve()  # Returns the optimal value.
print("status:", problem.status)
print("optimal value", problem.value)
print("optimal var", prices.value, betas.value)

#
