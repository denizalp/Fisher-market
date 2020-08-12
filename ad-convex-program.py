# %% 
import numpy as np
import cvxpy as cp
import fisher.fisherMarket as m
import dccp

#%%
num_buyers = 5
num_goods = 5


# Valuation of buyers: |buyers| x |goods|
valuations = np.random.rand(num_buyers, num_goods)
## Normalize rows
valuations = (valuations.T / valuations.sum(axis = 1)).T

# Endowment of buyers: |buyers| x |goods|
endows = np.random.rand(num_buyers, num_goods)
## Normalize columns
endows = endows / endows.sum(axis = 0)

allocs = []
for good in range(num_goods):
    allocs.append(cp.Variable((num_buyers, num_goods)))

obj_expr = 0

for i in range(num_buyers):
    for j in range(num_goods):
        obj_expr += (cp.log( np.sum(valuations[i,:].T @ allocs[j][i,:]) - valuations[i,j] * allocs[j][i,j] ))

expr_constraint = 0

for good in range(num_goods):
    expr_constraint += cp.sum(allocs[good], axis = 0)

variable_bounds = [ allocs[good] >= 0 for good in range(num_goods) ]
endow_bounds = [ allocs[good][:,good] <= endows[:,good] for good in range(num_goods) ]
constraints = [ expr_constraint <= 1 ]
constraints += variable_bounds + endow_bounds

obj = cp.Maximize(obj_expr)
primal = cp.Problem(obj, constraints)


# Solve Program
primal.solve()  # Returns the optimal value.

X = np.zeros((num_buyers, num_goods))
# Get primal maximizer (allocations)
for good in range(num_goods):
    X += allocs[good].value

# Get dual maximizer (prices) directly from CVXPY
p = constraints[0].dual_value

print(f"Allocations:\n{X}\n prices:\n{p}\n")
print(f"Budgets {endows @ p}\nSpending {X @ p}")

market = m.FisherMarket(valuations, endows @ p)
fX, prices = market.solveMarket("linear", printResults=False)

print(f"Fisher Prices:\n{prices}\nFisher budgets\n{endows @ p}\nFisher Spending\n{fX @ prices}")

# %% [markdown]

# Price adjustment process

num_buyers = 5
num_goods = 5
# Valuation of buyers: |buyers| x |goods|
valuations = np.random.rand(num_buyers, num_goods)
## Normalize rows
valuations = (valuations.T / valuations.sum(axis = 1)).T

# Endowment of buyers: |buyers| x |goods|
endows = np.random.rand(num_buyers, num_goods)
## Normalize columns
endows = endows / endows.sum(axis = 0)

iter = 0
prev_budgets = np.ones(num_goods)
prices = np.ones(num_goods)/num_goods
budgets = np.ones(num_buyers)/num_buyers

while (np.sum(np.abs(budgets - prev_budgets)) > 0.01 and iter <= 200):
    print(f"Iteration {iter}\nBudgets\n{budgets}")
    market = m.FisherMarket(valuations, budgets)
    X, p = market.solveMarket("leontief", printResults=False)
    excess_power = X @ p - budgets 
    prev_budgets = X @ p
    budgets += excess_power*0.1 
    iter += 1          
if (iter < 200):
    print("Process converged")

# %%


#%%

# Valuation of buyers: |buyers| x |goods|
valuations = np.array([[1, 2, 3], [2, 1, 3], [3, 2, 1]])
# Endowment of buyers: |buyers| x |goods|
endows = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

obj_expr = 0

for i in range(num_buyers):
    for j in range(num_goods):
        obj_expr += (cp.log( np.sum(valuations[i,:].T @ allocs[j][i,:]) - valuations[i,j] * allocs[j][i,j] ))

expr_constraint = 0

for good in range(num_goods):
    expr_constraint += cp.sum(allocs[good], axis = 0)

variable_bounds = [ allocs[good] >= 0 for good in range(num_goods) ]
endow_bounds = [ allocs[good][:,good] <= endows[:,good] for good in range(num_goods) ]
constraints = [ expr_constraint <= 1 ]
constraints += variable_bounds + endow_bounds

obj = cp.Maximize(obj_expr)
primal = cp.Problem(obj, constraints)


# Solve Program
primal.solve()  # Returns the optimal value.


#%%
num_buyers = 5
num_goods = 5

# Valuation of buyers: |buyers| x |goods|
valuations = np.random.rand(num_buyers, num_goods)
## Normalize rows
valuations = (valuations.T / valuations.sum(axis = 1)).T

# Endowment of buyers: |buyers| x |goods|
endows = np.random.rand(num_buyers, num_goods)
## Normalize columns
endows = endows / endows.sum(axis = 0)

allocs = cp.Variable(endows.shape)
value = cp.Variable(endows.shape[0])

print(f"Valuations\n{valuations}\nendows\n{endows}")
obj = cp.Maximize(  value.T @ cp.log(cp.sum(cp.multiply(valuations, allocs), axis = 1)))  

constraints = [cp.sum(allocs, axis = 0) <= np.sum(endows, axis = 0),
                cp.sum(value) <= 1,
                allocs >= 0]

problem = cp.Problem(obj, constraints)

problem.solve()
problem.status


#%%
X = allocs.value
p = constraints[0].dual_value
p = p/np.sum(p)

print(f"Allocations:\n{X}\n prices:\n{p}\n")
print(f"Budgets {endows @ p}\nSpending {X @ p}")

market = m.FisherMarket(valuations, endows @ p)
fX, prices = market.solveMarket("linear", printResults=False)

print(f"Fisher Prices:\n{prices}\nFisher budgets\n{endows @ p}\nFisher Spending\n{fX @ prices}")



# %%
allocs = cp.Variable(num_buyers, num_goods)
betas = cp.Variable(num_buyers)
obj = cp.Maximize(betas.T @ cp.log())