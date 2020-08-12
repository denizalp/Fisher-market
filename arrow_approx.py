#%%
import numpy as np
import fisher.fisherMarket as m
import matplotlib.pyplot as plt

# %% [markdown]
# # Example: Cobb-Douglas
def getPrices(prices, endows, valuations):
    return valuations.T @ (endows @ prices)

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[0.3,  0.7], [0.8, 0.2],[0.4, 0.6] ])



# Endowment of buyers: |buyers|
endows = np.array([[0.7, 0.5], [0.2, 0.1], [0.1, 0.4]])

print(f"Valuations\n{valuations}\nEndowments\n{endows}")

# Declare initial prices
prices = np.array([49/59, 49/59]) 
price_hist = [np.array([49/59, 49/59])]
prev_prices = np.array([100, 100])
iter = 0
while(np.sum(np.abs(prices - prev_prices)) > 0.001 and iter < 100):
    prev_prices = prices
    prices = getPrices(prices, endows, valuations)
    price_hist.append(prices)
    iter += 1

if(iter >= 100):
    print("The process has not converged")
else:
    print(f"The process has converged in {iter} iterations with prices\n{prices}")


#%% [markdown]
# ## Results
# ### Price of Good 1
price_hist = np.array(price_hist)
fig, ax = plt.subplots()
ax.plot([i for i in range(price_hist.shape[0])], price_hist[:,0], "-g", label = "Good 1")

plt.title("Price of Good 1 vs Iteration\n")
plt.xlabel("Iteration Number")
plt.ylabel("Price of good 1")

#%% [markdown]
# ### Price of Good 2
price_hist = np.array(price_hist)
fig, ax = plt.subplots()
ax.plot([i for i in range(price_hist.shape[0])], price_hist[:,1], "-g", label = "Good 1")

plt.title("Price of Good 2 vs iteration\n")
plt.xlabel("Iteration Number")
plt.ylabel("Price of good 2")


#%% [markdown]
# # Example: Linear

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1,  2], [2, 1]])


# Endowment of buyers: |buyers|
endows = np.array([[1, 0.25], [0, 0.75]])

print(f"Valuations\n{valuations}\nEndowments\n{endows}")

# Declare initial prices
prices = np.array([1, 1]) 
prev_prices = np.array([10, 10])
prev_diff = np.sum(np.abs(prices - prev_prices))
price_hist = [prices]
iter = 0

while (np.sum(np.abs(prices - prev_prices)) > 0.01 and iter < 100):
    
    # Store previous prices
    prev_prices = prices

    # Calculate new budgets
    budgets = endows @ prices 
    # Create Market
    market = m.FisherMarket(valuations, budgets)
    X, prices = market.solveMarket("linear", printResults=False)
    price_hist.append(prices)
    iter += 1


if(iter >= 100):
    print("The process has not converged")
else:
    print(f"The process has converged in {iter} iterations with prices\n{prices}")

#%% [markdown]
# ## Results
# ### Price of Good 1
price_hist = np.array(price_hist)
fig, ax = plt.subplots()
ax.plot([i for i in range(price_hist.shape[0])], price_hist[:,0], "-g", label = "Good 1")

plt.title("Price of Good 1 vs iteration\n")
plt.xlabel("Iteration Number")

#%% [markdown]
# ### Price of Good 2
price_hist = np.array(price_hist)
fig, ax = plt.subplots()
ax.plot([i for i in range(price_hist.shape[0])], price_hist[:,1], "-g", label = "Good 1")

plt.title("Price of Good 2 vs iteration\n")
plt.xlabel("Iteration Number")
plt.ylabel("Price of good 2")

#%% [markdown]
# # Example: Leontief

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[2,  6], [4, 1]])


# Endowment of buyers: |buyers|
endows = np.array([[1, 0.25], [0, 0.75]])

print(f"Valuations\n{valuations}\nEndowments\n{endows}")

# Declare initial prices
prices = np.array([1, 1]) 
prev_prices = np.array([10, 10])
price_hist = [prices]
iter = 0

while (np.sum(np.abs(prices - prev_prices)) > 0.01 and iter < 100):
    # Store previous prices
    prev_prices = prices

    # Calculate new budgets
    budgets = endows @ prices 

    # Create Market
    market = m.FisherMarket(valuations, budgets)
    X, prices = market.solveMarket("leontief", printResults=False)
    price_hist.append(prices)
    iter += 1

if(iter >= 100):
    print("The process has not converged")
else:
    print(f"The process has converged in {iter} iterations with prices\n{prices}")

#%% [markdown]
# ## Results
# ### Price of Good 1
price_hist = np.array(price_hist)
fig, ax = plt.subplots()
ax.plot([i for i in range(price_hist.shape[0])], price_hist[:,0], "-g", label = "Good 1")

plt.title("Price of Good 1 vs iteration\n")
plt.xlabel("Iteration Number")

#%% [markdown]
# ### Price of Good 2
price_hist = np.array(price_hist)
fig, ax = plt.subplots()
ax.plot([i for i in range(price_hist.shape[0])], price_hist[:,1], "-g", label = "Good 1")

plt.title("Price of Good 2 vs iteration\n")
plt.xlabel("Iteration Number")
plt.ylabel("Price of good 2")


#%% [markdown]
# # Example: Quasi-Linear

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1,  2], [2, 1]])


# Endowment of buyers: |buyers|
endows = np.array([[1, 0.25], [0, 0.75]])

print(f"Valuations\n{valuations}\nEndowments\n{endows}")

# Declare initial prices
prices = np.array([1, 1]) 
prev_prices = np.array([10, 10])
price_hist = [prices]
iter = 0

while (np.sum(np.abs(prices - prev_prices)) > 0.01 and iter < 100):
    # Store previous prices
    prev_prices = prices

    # Calculate new budgets
    budgets = endows @ prices 

    # Create Market
    market = m.FisherMarket(valuations, budgets)
    X, prices = market.solveMarket("quasi-linear", printResults=False)
    price_hist.append(prices)
    iter += 1

if(iter >= 100):
    print("The process has not converged")
else:
    print(f"The process has converged in {iter} iterations with prices\n{prices}")
#%% [markdown]
# ## Results
# ### Price of Good 1
price_hist = np.array(price_hist)
fig, ax = plt.subplots()
ax.plot([i for i in range(price_hist.shape[0])], price_hist[:,0], "-g", label = "Good 1")

plt.title("Price of Good 1 vs iteration\n")
plt.xlabel("Iteration Number")

#%% [markdown]
# ### Price of Good 2
price_hist = np.array(price_hist)
fig, ax = plt.subplots()
ax.plot([i for i in range(price_hist.shape[0])], price_hist[:,1], "-g", label = "Good 1")

plt.title("Price of Good 2 vs iteration\n")
plt.xlabel("Iteration Number")
plt.ylabel("Price of good 2")

#%% [markdown]
# # Example: CES with rho = 0.5

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1,  2], [2, 1]])


# Endowment of buyers: |buyers|
endows = np.array([[1, 0.25], [0, 0.75]])

print(f"Valuations\n{valuations}\nEndowments\n{endows}")

# Declare initial prices
prices = np.array([1, 1]) 
prev_prices = np.array([10, 10])
price_hist = [prices]
iter = 0

while (np.sum(np.abs(prices - prev_prices)) > 0.01 and iter < 100):
    print(f"Iteration {iter}\nPrices: {prices}")
    # Store previous prices
    prev_prices = prices

    # Calculate new budgets
    budgets = endows @ prices 

    # Create Market
    market = m.FisherMarket(valuations, budgets)
    X, prices = market.solveMarket("ces", printResults=False, rho = 0.5)
    price_hist.append(prices)
    iter += 1

if(iter >= 100):
    print("The process has not converged")
else:
    print(f"The process has converged in {iter} iterations with prices\n{prices}")

#%% [markdown]
# ## Results
# ### Price of Good 1
price_hist = np.array(price_hist)
fig, ax = plt.subplots()
ax.plot([i for i in range(price_hist.shape[0])], price_hist[:,0], "-g", label = "Good 1")

plt.title("Price of Good 1 vs iteration\n")
plt.xlabel("Iteration Number")

#%% [markdown]
# ### Price of Good 2
price_hist = np.array(price_hist)
fig, ax = plt.subplots()
print(prices.shape)
ax.plot([i for i in range(price_hist.shape[0])], price_hist[:,1], "-g", label = "Good 1")

plt.title("Price of Good 2 vs iteration\n")
plt.xlabel("Iteration Number")
plt.ylabel("Price of good 2")


#%% [markdown] 
# # Leontief closed form solution 

# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[0.20,  0.80], [0.8, 0.2]])


# Endowment of buyers: |buyers|
endows = np.array([[1, 0.25], [0, 0.75]])

# budgets of buyers: |buyers|
budgets = np.array([1, 1])

market = m.FisherMarket(valuations, budgets)
X, prices = market.solveMarket("leontief", printResults=False)
print(f"Fisher Market Prices: {prices}")

V_inv = np.linalg.inv(valuations) 
print(V_inv.T  )
print(np.diag(V_inv.T @ np.ones(2) ))
print("Calculated prices:\n",np.linalg.solve(np.diag(V_inv.T @ np.ones(2) ) @ valuations, budgets ))

# %%
