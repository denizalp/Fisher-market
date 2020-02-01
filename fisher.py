import numpy as np
import cvxpy as cp

###### Market Parameters ######


# Number of buyers in the market (row)
numberOfBuyers = 4

# Number of goods in the market (column)
numberOfGoods = 5

# Vector with quantity of goods: |goods|
numGoodsVec = np.array([1,2,6,4,3])

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1,3,5,1,2], [2,5,6,2,6], [6,3,5,1,4], [3,3,4,2,6]])

# Budgets of buyers: |buyers|
budgets = np.array([20, 23, 54, 12])



################################################################################
################################ Solver ########################################
################################################################################

##################### Quasi-Linear Fisher Market #####################

########### Primal: Output => Prices ###########

# Variables of program
prices = cp.Variable(numberOfGoods)
betas = cp.Variable(numberOfBuyers)

# Objective
obj = cp.Minimize(cp.sum(prices) - budgets.T @ cp.log(betas))

# Constraints
constraints = [prices[i] >= cp.multiply(valuations[i,], betas[i]) for i in range(numberOfBuyers)] + [betas <= 1]

# Convex Program for primal
primal = cp.Problem(obj, constraints)

# Solve Program
primal.solve()  # Returns the optimal value.
print("Status:", primal.status)
print("Optimal Value", primal.value)
print("Optimal Prices", prices.value, betas.value)

########### Dual: Output => Allocation #########

# Variables of program
alloc = cp.Variable((numberOfBuyers, numberOfGoods))
values = cp.Variable(numberOfBuyers)
utils = cp.Variable(numberOfBuyers)

# Objective
obj = cp.Maximize(cp.sum(cp.multiply(budgets, cp.log(utils)) - values))

constraints = [utils <= cp.sum(cp.multiply(valuations, alloc), axis = 1) + values,
                cp.sum(alloc, axis = 0) <= 1,
                alloc >= 0,
                values >= 0]

# Convex Program for dual
dual = cp.Problem(obj, constraints)


# Solve Program
dual.solve()  # Returns the optimal value.
print("Status:", dual.status)
print("Optimal Value", dual.value)
print("Optimal Allocation", alloc.value)


######################## Linear Fisher Market ########################

########### Primal: Output => Allocation #########

# Variables of program
alloc = cp.Variable((numberOfBuyers, numberOfGoods))
utils = cp.Variable(numberOfBuyers)

# Objective
obj = cp.Maximize(budgets.T @ cp.log(utils))

constraints = [utils <= cp.sum(cp.multiply(valuations, alloc), axis = 1),
                cp.sum(alloc, axis = 0) <= 1,
                alloc >= 0]

# Convex Program for primal
primal = cp.Problem(obj, constraints)


# Solve Program
primal.solve()  # Returns the optimal value.
print("Status:", primal.status)
print("Optimal Value", primal.value)
print("Optimal Allocation", alloc.value)


########### Primal: Output => Prices ###########

# Variables of program
prices = cp.Variable(numberOfGoods)
betas = cp.Variable(numberOfBuyers)

# Objective
obj = cp.Minimize(cp.sum(prices) - budgets.T @ cp.log(betas))

# Constraints
constraints = [prices[i] >= cp.multiply(valuations[i,], betas[i]) for i in range(numberOfBuyers)]

# Convex Program for primal
dual = cp.Problem(obj, constraints)

# Solve Program
dual.solve()  # Returns the optimal value.
print("Status:", dual.status)
print("Optimal Value", dual.value)
print("Optimal Prices", prices.value)
