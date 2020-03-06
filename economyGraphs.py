import numpy as np
import fisherMarket as m
import matplotlib.pyplot as plt
import economy as e

# Note, we assume that each firm produces one good, hence |goods|  = |firms|
# Furthermore since every worker is also a buyer |buyer| = |workers|

############################### Example 1 ######################################

# Matrix of valuations of buyers/workers: |buyers| x |goods|
demandV = np.array([[8.0, 2.0], [2.0, 5.0]])

# Matrix of valuations of firms: |firms| x |workers|
supplyV = np.array([[5.0, 3.0], [1.0, 5.0]])

# Budgets of firms: |buyers|
supplyB = np.array([0.0, 10.0])

iter = 0
budgets = []
prices = []

while(iter < 100):
    budgets.append(supplyB.tolist())
    supply = m.FisherMarket(V = supplyV, B = supplyB)
    supplyD, supplyS = supply.getDS("linear") # solve for demand & supply
    X, w = supply.getCache() # store the allocation

    # Create the new demand side market
    demand = m.FisherMarket(demandV, supplyD)
    demandD, demandS = demand.getDS("linear")  #solve for demand & supply

    Q, p = demand.getCache()
    B = supply.getBudgets()
    prices.append(p.tolist())
    supplyB[0]  += 0.1
    supplyB[1] -= 0.1
    iter += 1
budgets = np.array(budgets)
prices = np.array(prices)

############################## GRAPHS #################################
fig = plt.figure(figsize = (12,5))
ax1 = plt.subplot(1, 2, 1)
ax1.plot(budgets[:,0], prices[:,0], "-g", label = "Good 1")
ax1.plot(budgets[:,0], prices[:,1], "-b", label = "Good 2")
plt.title("Input price vs. Output Prices 1\n Good Valuations: [8.0, 2.0], [2.0, 5.0]\nWorker Valuations: [5.0, 3.0], [1.0, 5.0]")
plt.xlabel("Input price good 1")
plt.ylabel("Output prices")

ax2 = plt.subplot(1, 2, 2)
ax2.plot(budgets[:,1], prices[:,0], "-g", label = "Good 1")
ax2.plot(budgets[:,1], prices[:,1], "-b", label = "Good 2")
plt.title("Input price vs. Output Prices 1\n Good Valuations: [8.0, 2.0], [2.0, 5.0]\nWorker Valuations: [5.0, 3.0], [1.0, 5.0]")
plt.xlabel("Input price good 2")
plt.ylabel("Output prices")
plt.legend()
plt.savefig("./experiments/economy/graph1.png")

### Prices Substracted : to check roots###

fig = plt.figure(figsize = (12,5))
ax1 = plt.subplot(1, 2, 1)
ax1.plot(budgets[:,0], (prices[:,0] - budgets[:,0]), "-g", label = "Good 1")
ax1.plot(budgets[:,0], (prices[:,1] - budgets[:,1]), "-b", label = "Good 2")
plt.title("Input price vs. Output Prices 1\n Good Valuations: [8.0, 2.0], [2.0, 5.0]\nWorker Valuations: [5.0, 3.0], [1.0, 5.0]")
plt.xlabel("Input price good 1")
plt.ylabel("Output prices")

ax2 = plt.subplot(1, 2, 2)
ax2.plot(budgets[:,1], (prices[:,0] - budgets[:,0]), "-g", label = "Good 1")
ax2.plot(budgets[:,1], (prices[:,1] - budgets[:,1]), "-b", label = "Good 2")
plt.title("Input price vs. Output Prices 1\n Good Valuations: [8.0, 2.0], [2.0, 5.0]\nWorker Valuations: [5.0, 3.0], [1.0, 5.0]")
plt.xlabel("Input price good 2")
plt.ylabel("Output prices")
plt.legend()
plt.savefig("./experiments/economy/graph1roots.png")

# Check eqm price vector

# Create Market
market1 = e.Economy(supplyV, supplyB, demandV)

# Check if the iterative process converges
Q, p, X, w, B = market1.solve(0.001, "linear", printResults = True) # For this one definitely contraction



############################### Example 1 ######################################

# Matrix of valuations of buyers/workers: |buyers| x |goods|
demandV = np.array([[8.0, 2.0], [2.0, 5.0]])

# Matrix of valuations of firms: |firms| x |workers|
supplyV = np.array([[5.0, 3.0], [1.0, 5.0]])

# Budgets of firms: |buyers|
supplyB = np.array([0.0, 10.0])

iter = 0
budgets = []
prices = []

while(iter < 100):
    budgets.append(supplyB.tolist())
    supply = m.FisherMarket(V = supplyV, B = supplyB)
    supplyD, supplyS = supply.getDS("quasi-linear") # solve for demand & supply
    X, w = supply.getCache() # store the allocation

    # Create the new demand side market
    demand = m.FisherMarket(demandV, supplyD)
    demandD, demandS = demand.getDS("linear")  #solve for demand & supply


    Q, p = demand.getCache()
    B = supply.getBudgets()
    prices.append(p.tolist())
    supplyB[0]  += 0.1
    supplyB[1] -= 0.1
    iter += 1
budgets = np.array(budgets)
prices = np.array(prices)

############################## GRAPHS #################################
fig = plt.figure(figsize = (12,5))
ax1 = plt.subplot(1, 2, 1)
ax1.plot(budgets[:,0], prices[:,0], "-g", label = "Good 1")
ax1.plot(budgets[:,0], prices[:,1], "-b", label = "Good 2")
plt.title("Input price vs. Output Prices 1\n Good Valuations: [8.0, 2.0], [2.0, 5.0]\nWorker Valuations: [5.0, 3.0], [1.0, 5.0]")
plt.xlabel("Input price good 1")
plt.ylabel("Output prices")

ax2 = plt.subplot(1, 2, 2)
ax2.plot(budgets[:,1], prices[:,0], "-g", label = "Good 1")
ax2.plot(budgets[:,1], prices[:,1], "-b", label = "Good 2")
plt.title("Input price vs. Output Prices 1\n Good Valuations: [8.0, 2.0], [2.0, 5.0]\nWorker Valuations: [5.0, 3.0], [1.0, 5.0]")
plt.xlabel("Input price good 2")
plt.ylabel("Output prices")
plt.legend()


### Prices Substracted : to check roots###

fig = plt.figure(figsize = (12,5))
ax1 = plt.subplot(1, 2, 1)
ax1.plot(budgets[:,0], (prices[:,0] - budgets[:,0]), "-g", label = "Good 1")
ax1.plot(budgets[:,0], (prices[:,1] - budgets[:,1]), "-b", label = "Good 2")
plt.title("Input price vs. Output Prices 1\n Good Valuations: [8.0, 2.0], [2.0, 5.0]\nWorker Valuations: [5.0, 3.0], [1.0, 5.0]")
plt.xlabel("Input price good 1")
plt.ylabel("Output prices")

ax2 = plt.subplot(1, 2, 2)
ax2.plot(budgets[:,1], (prices[:,0] - budgets[:,0]), "-g", label = "Good 1")
ax2.plot(budgets[:,1], (prices[:,1] - budgets[:,1]), "-b", label = "Good 2")
plt.title("Input price vs. Output Prices 1\n Good Valuations: [8.0, 2.0], [2.0, 5.0]\nWorker Valuations: [5.0, 3.0], [1.0, 5.0]")
plt.xlabel("Input price good 2")
plt.ylabel("Output prices")
plt.legend()
