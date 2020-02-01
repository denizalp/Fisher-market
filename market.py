import numpy as np
import cvxpy as cp

class Market(object):
    """
    This is a class that models a Market

    Attributes:
        valutations (numpy: double x double):
            matrix of valuations of buyer i for good j.
        budgets (numpy: double): vector of buyer budgets.
        numGoodsVec (numpy: double): vector of number of each good.

    """

    def __init__(self, V, B, M):
        """
        The constructor for the market class.

        Parameters:
        V (numpy: double x double): matrix of valuations of buyer i for good j.
        B (numpy: double): vector of buyer budgets.
        M (numpy: double): vector of number of each good.
        """
        self.valuations = V
        self.budgets = B
        self.numGoodsVec = M

    def numberOfGoods():
        """
        Returns:
        Number of goods in the market
        """
        return self.numGoodsVec.size()

    def numberOfBuyers():
        """
        Returns:
        Number of buyers in the market
        """
        return self.budgets.size()

    def solveMarket(utilities = "quasi-linear"):
        """
        Parameters:
        utilities(string): Denotes the utilities used to solve market
            Currently options are 'quasi-linear' and 'linear'

        Returns:
        A tuple (X, p) that corresponds to the optimal matrix of allocations and
        prices.
        """
        if utilities = "quasi-linear":
            return self.solveQuasiLinear()
        elif utilities = "linear":
            return self.solveLinear()
        else:
            print("Invalid Utility Model")
            exit(0)

    def solveQuasiLinear():

        ##################### Quasi-Linear Fisher Market #####################

        ########### Primal: Output => Prices ###########

        numberOfGoods = self.numberOfGoods()
        numberOfBuyers = self.numberOfBuyers()

        # Variables of program
        prices = cp.Variable(numberOfGoods)
        betas = cp.Variable(numberOfBuyers)

        # Objective
        obj = cp.Minimize(cp.sum(prices) - budgets.T @ cp.log(betas))

        # Constraints
        constraints = [prices[i] >= cp.multiply(valuations[i,], betas[i]) \
                        for i in range(numberOfBuyers)] + [betas <= 1]

        # Convex Program for primal
        primal = cp.Problem(obj, constraints)

        # Solve Program
        primal.solve()  # Returns the optimal value.
        print("Status:", primal.status)
        #print("Optimal Value", primal.value)
        #print("Optimal Prices", prices.value, betas.value)


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
