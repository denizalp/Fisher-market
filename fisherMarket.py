import cvxpy as cp
import numpy as np

class FisherMarket:
    """
    This is a class that models a Fisher Market

    Attributes:
        valutations (numpy: double x double):
            matrix of valuations of buyer i for good j.
        budgets (numpy: double): vector of buyer budgets.
        numGoodsVec (numpy: double): vector of number of each good.

    """

    def __init__(self, V, B, M = None):
        """
        The constructor for the fisherMarket class.

        Parameters:
        valuations (numpy: double x double): matrix of valuations of buyer i for good j.
        budgets (numpy: double): vector of buyer budgets.
        numGoodsVec (numpy: double): vector of number of each good.
        """
        self.budgets = B

        if(M is None):
            self.valuations = V
            self.numGoodsVec = np.ones(self.valuations.shape[1])
        else:
            self.numGoodsVec = M
            # Add each copy of a good as a new good with the same valuation to the
            # valuations matrix
            self.valuations = np.empty((0,self.numberOfBuyers()))
            for item, itemNumber in enumerate(self.numGoodsVec):
                self.valuations = np.append(self.valuations, np.tile(V[:,item], (itemNumber, 1)), axis =0)
            self.valuations = self.valuations.T


    def getBudgets(self):
        """
        Returns:
        The budgets of the buyers in the market
        """
        return self.budgets
    def getValuations(self):
        """
        Returns:
        The valuation of buyers in the market
        """
        return self.valuations

    def numberOfGoods(self):
        """
        Returns:
        Number of goods in the market
        """
        return self.numGoodsVec.size

    def numberOfBuyers(self):
        """
        Returns:
        Number of buyers in the market
        """
        return self.budgets.size

    def getCache(self):
        """
        Returns:
        The cached alocation values (X, p)

        """
        return (self.optimalX, self.optimalp)

    def getDS(self, utilities = "quasi-linear"):
        """
        Takes as input the utility structure and returns the demand and supply
        (in dollars) of all goods in the economy.

        Parameters:
        utilities(string): Denotes the utilities used to solve market
            Currently options are 'quasi-linear' and 'linear'

        Returns:
        A tuple (D, S) of vector of demand and supply for each good.
        """
        # Find optimal allocation and cache it
        X,p = self.solveMarket(utilities)
        self.optimalX = X
        self.optimalp = p

        D = np.sum(X*p, axis = 0)
        assert D.size == self.numberOfGoods()

        S = np.multiply(self.numGoodsVec, p)
        assert S.size == self.numberOfGoods()
        assert (np.sum(np.abs(D-S)) < 0.0001)

        return (D, S)

    def solveMarket(self, utilities = "quasi-linear"):
        """
        Parameters:
        utilities(string): Denotes the utilities used to solve market
            Currently options are 'quasi-linear' and 'linear'

        Returns:
        A tuple (X, p) that corresponds to the optimal matrix of allocations and
        prices.
        """
        if (utilities == "quasi-linear"):
            alloc, prices = self.solveQuasiLinear()
        elif (utilities == "linear"):
            alloc, prices = self.solveLinear()
        else:
            print(f"Invalid Utility Model : '{utilities}'")
            exit()

        # print( f"prices before = {prices}\n")
        itemCounter = 0
        itemNumber = 0
        X = np.zeros((self.numberOfBuyers(), self.numberOfGoods()))
        p = []
        for item in range(self.valuations.shape[1]):
            # print(f"itemNumber = {itemNumber}, itemCounter = {itemCounter}, numGood = {self.numGoodsVec[itemNumber]}")
            X[:, itemNumber] += alloc[:,item]
            itemCounter += 1

            if (itemCounter == self.numGoodsVec[itemNumber]):
                p.append(prices[item])
                itemNumber += 1
                itemCounter = 0

        p = np.array(p)
        # print( f"prices after = {p}\n")
        return (X,p)

    def solveQuasiLinear(self):
        """
        Solves Fisher Market with Quasi-Linear utilities

        Returns:
        A tuple (X, p) that corresponds to the optimal matrix of allocations and
        prices.
        """
        numberOfGoods = np.sum(self.numGoodsVec).astype(int)
        numberOfBuyers = self.numberOfBuyers()

        ########### Primal: Output => Prices ###########

        # Variables of program
        prices = cp.Variable(numberOfGoods)
        betas = cp.Variable(numberOfBuyers)

        # Objective
        obj = cp.Minimize(cp.sum(prices) - self.budgets.T @ cp.log(betas))

        # Constraints
        constraints = [prices[j] >= cp.multiply(self.valuations[:,j], betas) for j in range(numberOfGoods)] + [betas <= 1]


        # Convex Program for primal
        primal = cp.Problem(obj, constraints)

        # Solve Program
        primal.solve()  # Returns the optimal value.
        # print("Primal Status (Price): ", primal.status)
        # print("Optimal Value Primal (Price): ", primal.value)
        p = prices.value

        ########### Dual: Output => Allocation #########

        # Variables of program
        alloc = cp.Variable((numberOfBuyers, numberOfGoods))
        values = cp.Variable(numberOfBuyers)
        utils = cp.Variable(numberOfBuyers)

        # Objective
        obj = cp.Maximize(cp.sum(cp.multiply(self.budgets, cp.log(utils)) - values))

        constraints = [utils <= cp.sum(cp.multiply(self.valuations, alloc), axis = 1) + values,
                        cp.sum(alloc, axis = 0) <= 1,
                        alloc >= 0,
                        values >= 0]

        # Convex Program for dual
        dual = cp.Problem(obj, constraints)


        # Solve Program
        dual.solve()  # Returns the optimal value.
        # print("Dual Status (Allocation):", dual.status)
        # print("Optimal Value Dual (Allocation)", dual.value)
        X = alloc.value

        return (X, p)

    def solveLinear(self):
        """
        Solves Fisher Market with Linear utilities

        Returns:
        A tuple (X, p) that corresponds to the optimal matrix of allocations and
        prices.
        """

        numberOfGoods = np.sum(self.numGoodsVec).astype(int)
        numberOfBuyers = self.numberOfBuyers()

        ########### Primal: Output => Allocation #########

        # Variables of program
        alloc = cp.Variable((numberOfBuyers, numberOfGoods))
        utils = cp.Variable(numberOfBuyers)

        # Objective
        obj = cp.Maximize(self.budgets.T @ cp.log(utils))

        constraints = [utils <= cp.sum(cp.multiply(self.valuations, alloc), axis = 1),
                        cp.sum(alloc, axis = 0) <= 1,
                        alloc >= 0]

        # Convex Program for primal
        primal = cp.Problem(obj, constraints)


        # Solve Program
        primal.solve()  # Returns the optimal value.
        # print("Primal Status (Allocation):", primal.status)
        # print("Optimal Value Primal (Allocation)", primal.value)
        X = alloc.value


        ########### Primal: Output => Prices ###########

        # Variables of program
        prices = cp.Variable(numberOfGoods)
        betas = cp.Variable(numberOfBuyers)

        # Objective
        obj = cp.Minimize(cp.sum(prices) - self.budgets.T @ cp.log(betas))

        # Constraints
        constraints = [prices[j] >= cp.multiply(self.valuations[:,j], betas) for j in range(numberOfGoods)]

        # Convex Program for primal
        dual = cp.Problem(obj, constraints)

        # Solve Program
        dual.solve()  # Returns the optimal value.
        # print("Dual Status (Price): ", dual.status)
        # print("Optimal Value Dual (Price): ", dual.value)
        p = prices.value

        return (X, p)
