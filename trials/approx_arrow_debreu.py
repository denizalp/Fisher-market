#%%
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir) 
sys.path.insert(0,parentdir) 
import numpy as np
from fisher import fisherMarket as m

#%%
# # Example 4: Cobb-Douglas

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1,  2], [2, 1]])


# Budgets of buyers: |buyers|
endow = np.array([[4,  3], [2, 5]])



# Solve for market prices and allocations for desired utility function structure.

prices_prev = np.zeros(2)
prices = np.array([2, 1])
iter = 0

while (np.sum(np.abs(prices - prices_prev)) > 0.01 and iter < 200):
    prices_prev = prices
    budgets = endow @ prices
    market = m.FisherMarket(valuations, budgets)
    X, prices = market.solveMarket("linear", printResults=False)
    print(f"iter = {iter}\nPrices = {prices}\nPrevPrices = {prices_prev}")
    iter += 1
if (iter < 199 ):
    print("CONVERGED")    

# %%
