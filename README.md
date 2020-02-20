# Fisher-market
Fisher markets and associated solvers.
A market is built in `market.py`. You can declare parameters of the market in `fisherExample.py` and solve for market prices depending on the type of utility function you would like to use using the structure in `fisherExample.py`.

The project currently supports "linear" and "quasi-linear" utilities. You can solve the market with the function `solveMarket()` and passing it as argument the utility structure you desire as a string:

```{python}
# Matrix of valuations: |buyers| x |goods|
valuations = np.array([[1,3,5,1,2], [2,5,6,2,6],
    [6,3,5,1,4], [3,3,4,2,6]])

# Budgets of buyers: |buyers|
budgets = np.array([20, 23, 54, 12])

# Vector with quantity of goods: |goods|
numGoodsVec = np.array([1,2,6,4,3])

# Create Market
market1 = m.Market(valuations, budgets, numGoodsVec)

# Solve for market prices and allocations for
# desired utility function structure.

# Current Options are 'quasi-linear' and 'linear'
market1.solveMarket("quasi-linear")
market1.solveMarket("linear")

```

Note, the linear program is formulated, assuming that there is only one unit of each good in the market. In order to get around this, for each copy of a good, an extra column with the exact same preference for the good is added to the valuations matrix. Then, the original convex program can be solved to find the optimal prices and allocation.




Arrow debreu model with functions but that has demand side that takes wages as input, prove that model has equilibrium ans discuss the conseqences of the shape of the curves on model. Because for instance supply side curve takes prices and outputs wages, this is basically a measure of corpoarte profit, so it basically means inequality

the cycle thing also can explain how you can lose money on equilibrium even if you start with budget
