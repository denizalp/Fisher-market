#%%
import numpy as np
import fisher.fisherMarket as m
import matplotlib.pyplot as plt
from numpy import linalg as la
import cvxpy as cp

#%%

valuations = np.array([[1, 1, 1], [2, 1, 0], [0, 0, 3]])
endows = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
price_in1 = np.array([1, 0, 0])
price_in2 = np.array([0, 1, 0])
price_in3 = np.array([0, 0, 1])
market1 = m.FisherMarket(valuations, endows @ price_in1)
market2 = m.FisherMarket(valuations, endows @ price_in2)
market3 = m.FisherMarket(valuations, endows @ price_in3)
market4 = m.FisherMarket(valuations, endows @ (price_in1 + price_in2 + price_in3))
_, price_out1 = market1.solveMarket(utilities= "linear", printResults=False)
_, price_out2 = market2.solveMarket(utilities= "linear", printResults=False)
_, price_out3 = market3.solveMarket(utilities= "linear", printResults=False)
_, price_out4 = market4.solveMarket(utilities= "linear", printResults=False)

print(f"Price of market 1: {price_out1}\nPrice of market 2: {price_out2}\nPrice of market 3: {price_out3}\nPrice of Comination of Market: {price_out4}\nCombination of market prices {price_out1 + price_out2 + price_out3}")
iterate_linear(np.ones(3), endows, valuations)
# %% [markdown]
# # Example: Cobb-Douglas
def get_prices_cobb_douglas(prices, endows, valuations):
    return valuations.T @ (endows @ prices)

def iterate_cobb_douglas(prices, endows, valuations, max_iter = 200, epsilon = 0.01, print_results = False):
    prev_prices = np.ones(prices.shape)
    iter = 0
    while (np.sum(np.abs(prices - prev_prices)) > epsilon and iter <= max_iter):
        if(print_results == True):
            print(f"Iteration {iter}-Prices:\n{prices}")
        converged = True
        iter += 1
        prev_prices = prices
        prices = get_prices_cobb_douglas(prices, endows, valuations)

    if (iter >= max_iter):
        print("Iteration did not converge")
        converged = False
    return (converged, valuations, endows)

# %%
# Analyze experiments that do not converge if there are any
valuations = np.array([[1, 0], [0, 1]])
endows = np.array([[1, 0], [0, 1]])
prices = np.array([2/3, 1/3])


# %%
prices = get_prices_cobb_douglas(prices, endows, valuations)
prices


#%%
# Number of Agents
num_agents = 30

# Number of Commodities
num_commods = 40

# Number of experiments
num_experiments = 10000

failed_experiments = []
for experiment in range(num_experiments):
    # Matrix of valuations: |buyers| x |goods|
    valuations = np.random.rand(num_agents, num_commods) 
    ## Normalize rows
    valuations = (valuations.T / valuations.sum(axis = 1)).T
    
    # Endowment of buyers: |buyers| x |goods|
    endows = np.random.rand(num_agents, num_commods) 
    ## Normalize columns
    endows = endows / endows.sum(axis = 0)

    # Inital prices
    prices = np.ones(num_commods)/num_commods
    results = iterate_cobb_douglas(prices, endows, valuations)
    if (results[0] == False):
        failed_experiments.append(results[1:])
if(len(failed_experiments) == 0):
    print("ALL EXPERIMENTS HAVE CONVERGED")



# %% [markdown]

# Analysis of Leontief 

def get_prices_leontief(prices, endows, valuations):
    budgets = endows @ prices

    prices_out = cp.Variable(prices.shape[0])

    obj = cp.Minimize(cp.sum(prices_out) - budgets.T @ cp.log(valuations @ prices_out))
    constraints = [prices_out >= 0]

    program = cp.Problem(obj, constraints)
    
    program.solve()
    return prices_out.value

def iterate_leontief(prices, endows, valuations, max_iter = 400, epsilon = 0.05, alpha = 0.6, print_results = False):
    prev_prices = np.ones(prices.shape)
    iter = 0
    
    while (np.sum(np.abs(prices - prev_prices)) > epsilon and iter <= max_iter):
        if(print_results == True):
            print(f"Iteration {iter}-Prices:\n{prices}")
        converged = True
        iter += 1
        prev_prices = prices
        prices = prices*alpha + (1-alpha)*get_prices_leontief(prices, endows, valuations)
    if (iter >= max_iter):
        print("Iteration did not converge")
        converged = False
    return (converged, valuations, endows, prices)


#%%
# Number of Agents
num_agents = 5

# Number of Commodities
num_commods = 10

# Number of experiments
num_experiments = 1000
experiments = []
failed_experiments = []
for experiment in range(num_experiments):
    print(f"Experiment {experiment}\n")
    # Matrix of valuations: |buyers| x |goods|
    valuations = np.random.randint( low = 10, size = (num_agents, num_commods)) 
    
    # Endowment of buyers: |buyers| x |goods|
    endows = np.random.randint(low = 10, size = (num_agents, num_commods)) 
    endows = endows / endows.sum(axis = 0)

    # Inital prices
    prices = np.ones(num_commods)/num_commods
    results = iterate_leontief(prices, endows, valuations, print_results= False)
    experiments.append(results)
    if (results[0] == False):
        failed_experiments.append(results[1:])
if(len(failed_experiments) == 0):
    print("ALL EXPERIMENTS HAVE CONVERGED")

# %%
# Analyze experiments that do not converge if there are any
valuations = np.array([[1, 0], [0, 1]])
endows = np.array([[0, 1], [1, 0]])
prices = np.array([2/3, 1/3])


# %%
prices = get_prices_leontief(prices, endows, valuations)
prices


# %% [markdown]

# Analysis of Linear 

def get_prices_linear(prices, endows, valuations):
    market = m.FisherMarket(valuations, endows @ prices)
    X, p = market.solveMarket(utilities = "linear", printResults= False)
    return p

def iterate_linear(prices, endows, valuations, max_iter = 100, epsilon = 0.05, print_results = False):
    prev_prices = np.ones(prices.shape)
    iter = 0
    
    while (np.sum(np.abs(prices - prev_prices)) > epsilon and iter <= max_iter):
        if(print_results == True):
            print(f"Iteration {iter}-Prices:\n{prices}")
        converged = True
        iter += 1
        prev_prices = prices
        prices = get_prices_linear(prices, endows, valuations)
    if (iter >= max_iter):
        print("Iteration did not converge")
        converged = False
    return (converged, valuations, endows, prices)



#%%
# Number of Agents
num_agents = 5

# Number of Commodities
num_commods = 10

# Number of experiments
num_experiments = 10000
experiments = []
failed_experiments = []
for experiment in range(num_experiments):
    print(f"Experiment {experiment}\n")
    # Matrix of valuations: |buyers| x |goods|
    valuations = np.random.randint( low = 10, size = (num_agents, num_commods))
    
    # Endowment of buyers: |buyers| x |goods|
    endows = np.random.randint(low = 10, size = (num_agents, num_commods)) 
    endows = endows / endows.sum(axis = 0)

    # Inital prices
    prices = np.ones(num_commods)/num_commods
    results = iterate_linear(prices, endows, valuations, print_results= False)
    experiments.append(results)
    if (results[0] == False):
        failed_experiments.append(results[1:])
if(len(failed_experiments) == 0):
    print("ALL EXPERIMENTS HAVE CONVERGED")

# %%
valuations = np.array([[1, 0], [0, 1]])
endows = np.array([[0.1, 0.9], [0.9, 0.1]])
prices = np.array([0.7, 0.3])

# %%
prices = get_prices_linear(prices, endows, valuations)
prices

# %%
failed_experiments_perturb = []
for exper in failed_experiments:
    valuations, endows, prices = exper
    valuations = valuations.astype(np.float64) + np.random.rand(valuations.shape[0], valuations.shape[1])
    prices = np.ones(prices.shape)/prices.shape
    results = iterate_leontief(prices, endows, valuations, print_results= False)
    
    if (results[0] == False):
        failed_experiments_perturb.append(results[1:])
if(len(failed_experiments_perturb) == 0):
    print("ALL EXPERIMENTS HAVE CONVERGED")

# %%
