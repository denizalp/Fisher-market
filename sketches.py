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
