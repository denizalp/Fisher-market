#%%
import numpy as np
import fisher.fisherMarket as m
import matplotlib.pyplot as plt


#%% [markdown]
# # Example: Linear

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1,  2], [2, 1]])


# Endowment of buyers: |buyers|
endows = np.array([[1, 0.25], [0, 0.75]])

# Declare initial prices
prices = np.array([1, 1]) 
prev_prices = np.array([10, 10])

iter = 0

while (np.sum(np.abs(prices - prev_prices)) > 0.1 and iter < 200):
    print(f"Iteration {iter}\nPrices: {prices}")
    # Store previous prices
    prev_prices = prices

    # Calculate new budgets
    budgets = endows @ prices 

    # Create Market
    market = m.FisherMarket(valuations, budgets)
    X, prices = market.solveMarket("linear", printResults=False)
    
    iter += 1


if (iter < 200):
    print(f"Converged in {iter} iterations with prices:\n{prices}")



#%% [markdown]
# # Example: Leontief

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1,  2], [2, 1]])


# Endowment of buyers: |buyers|
endows = np.array([[1, 0.25], [0, 0.75]])

# Declare initial prices
prices = np.array([1, 1]) 
prev_prices = np.array([10, 10])

iter = 0

while (np.sum(np.abs(prices - prev_prices)) > 0.1 and iter < 200):
    print(f"Iteration {iter}\nPrices: {prices}")
    # Store previous prices
    prev_prices = prices

    # Calculate new budgets
    budgets = endows @ prices 

    # Create Market
    market = m.FisherMarket(valuations, budgets)
    X, prices = market.solveMarket("leontief", printResults=False)
    
    iter += 1

if (iter < 200):
    print(f"Converged in {iter} iterations with prices:\n{prices}")

#%% [markdown]
# # Example: Cobb-Douglas

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1,  2], [2, 1]])


# Endowment of buyers: |buyers|
endows = np.array([[1, 0.25], [0, 0.75]])

# Declare initial prices
prices = np.array([1, 1]) 
prev_prices = np.array([10, 10])

iter = 0

while (np.sum(np.abs(prices - prev_prices)) > 0.1 and iter < 200):
    print(f"Iteration {iter}\nPrices: {prices}")
    # Store previous prices
    prev_prices = prices

    # Calculate new budgets
    budgets = endows @ prices 

    # Create Market
    market = m.FisherMarket(valuations, budgets)
    X, prices = market.solveMarket("cobb-douglas", printResults=False)
    
    iter += 1

if (iter < 200):
    print(f"Converged in {iter} iterations with prices:\n{prices}")



#%% [markdown]
# # Example: cobb-douglas

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[0.25,  0.75], [0.75, 0.25]])


# Endowment of buyers: |buyers|
endows = np.array([[1, 0.25], [0, 0.75]])

# Declare initial prices
prices = np.array([1, 1]) 
prev_prices = np.array([10, 10])

iter = 0

while (np.sum(np.abs(prices - prev_prices)) > 0.01 and iter < 200):
    print(f"Iteration {iter}\nPrices: {prices}")
    # Store previous prices
    prev_prices = prices

    # Calculate new budgets
    budgets = endows @ prices 

    # Create Market
    market = m.FisherMarket(valuations, budgets)
    X, prices = market.solveMarket("cobb-douglas", printResults=False)
    
    iter += 1

if (iter < 200):
    print(f"Converged in {iter} iterations with prices:\n{prices}")

#%% [markdown]
# # Example: Quasi-Linear

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1,  2], [2, 1]])


# Endowment of buyers: |buyers|
endows = np.array([[1, 0.25], [0, 0.75]])

# Declare initial prices
prices = np.array([1, 1]) 
prev_prices = np.array([10, 10])

iter = 0

while (np.sum(np.abs(prices - prev_prices)) > 0.01 and iter < 200):
    print(f"Iteration {iter}\nPrices: {prices}")
    # Store previous prices
    prev_prices = prices

    # Calculate new budgets
    budgets = endows @ prices 

    # Create Market
    market = m.FisherMarket(valuations, budgets)
    X, prices = market.solveMarket("quasi-linear", printResults=False)
    
    iter += 1

if (iter < 200):
    print(f"Converged in {iter} iterations with prices:\n{prices}")



#%% [markdown]
# # Example: CES with rho = 0.5

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1,  2], [2, 1]])


# Endowment of buyers: |buyers|
endows = np.array([[1, 0.25], [0, 0.75]])

# Declare initial prices
prices = np.array([1, 1]) 
prev_prices = np.array([10, 10])

iter = 0

while (np.sum(np.abs(prices - prev_prices)) > 0.01 and iter < 200):
    print(f"Iteration {iter}\nPrices: {prices}")
    # Store previous prices
    prev_prices = prices

    # Calculate new budgets
    budgets = endows @ prices 

    # Create Market
    market = m.FisherMarket(valuations, budgets)
    X, prices = market.solveMarket("ces", printResults=False, rho = 0.5)
    
    iter += 1

if (iter < 200):
    print(f"Converged in {iter} iterations with prices:\n{prices}")


# %%
