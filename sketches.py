
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
constraints = [prices[j] >= cp.multiply(valuations[:,j], betas) for j in range(numberOfGoods)] + [betas <= 1]


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
constraints = [prices[j] >= cp.multiply(valuations[:,j], betas) for j in range(numberOfGoods)]

# Convex Program for primal
dual = cp.Problem(obj, constraints)

# Solve Program
dual.solve()  # Returns the optimal value.
print("Status:", dual.status)
print("Optimal Value", dual.value)
print("Optimal Prices", prices.value)


## Tried solving quasi-linear market in scipy did not work for some reason
## moved to cvxpy
import numpy as np
from scipy.optimize import minimize

#################################### SCIPY ####################################
## initial guesses ##

# Initial price guess:  |Goods|
prices0 = [3, 3, 3, 3, 3]

# Initial betas guess: |buyers|
betas0 = [0.3, 0.3, 0.3, 0.3]

# Merge variables into one array
params0 = prices0 + betas0

## Objective function ##
def objective(params):
    prices = params0[:len(prices0)]
    betas = params0[len(prices0):]
    return np.sum(prices) - budgets.T @ np.log(betas)

## Constraints ##
def constraint1(params):
    prices = params0[:len(prices0)]
    betas = params0[len(prices0):]
    return prices - valuations @ betas


# show initial objective
print('Initial Objective: ' + str(objective(params0)))
# print("Constraints: " + )

# Set bounds and constraints
bnds = [(None, None) for _ in prices0] + [(None, 1) for _ in betas0]
cons1 = {'type': 'ineq', 'fun': constraint1}
cons = [cons1]

solution = minimize(objective, params0, method='SLSQP',\
                    bounds=bnds, constraints=cons)
