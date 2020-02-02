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
        """
        Solves Fisher Market with Quasi-Linear utilities

        Returns:
        A tuple (X, p) that corresponds to the optimal matrix of allocations and
        prices.
        """
        numberOfGoods = self.numberOfGoods()
        numberOfBuyers = self.numberOfBuyers()


        ########### Primal: Output => Prices ###########

        # Variables of program
        prices = cp.Variable(numberOfGoods)
        betas = cp.Variable(numberOfBuyers)

        # Objective
        obj = cp.Minimize(cp.sum(prices) - budgets.T @ cp.log(betas))

        # Constraints
        constraints = [prices[j] >= cp.multiply(valuations[:,j], betas) for j in range(numberOfGoods)] + [betas <= 1]


        # Convex Program for primal
        primal = cp.Problem(obj, constraints)

        # Solve Program
        primal.solve()  # Returns the optimal value.
        print("Primal Status (Price): ", primal.status)
        print("Optimal Value Primal (Price): ", primal.value)
        p = prices.value

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
        print("Dual Status (Allocation):", dual.status)
        print("Optimal Value Dual (Allocation)", dual.value)
        X = alloc.value

        return (X, p)

    def solveLinear():
        """
        Solves Fisher Market with Linear utilities

        Returns:
        A tuple (X, p) that corresponds to the optimal matrix of allocations and
        prices.
        """

        numberOfGoods = self.numberOfGoods()
        numberOfBuyers = self.numberOfBuyers()

        ########### Primal: Output => Allocation #########

        # Variables of program
        alloc = cp.Variable((numberOfBuyers, numberOfGoods))
        utils = cp.Variable(numberOfBuyers)

        # Objective
        obj = cp.Maximize(budgets.T @ cp.log(utils))

        constraints = [utils <= cp.sum(cp.multiply(valuations, alloc), axis = 1),
                        cp.sum(alloc, axis = 0) <= 1,
                        alloc >= 0]

        # Convex Program for primal
        primal = cp.Problem(obj, constraints)


        # Solve Program
        primal.solve()  # Returns the optimal value.
        print("Primal Status (Allocation):", primal.status)
        print("Optimal Value Primal (Allocation)", primal.value)
        X = alloc.value


        ########### Primal: Output => Prices ###########

        # Variables of program
        prices = cp.Variable(numberOfGoods)
        betas = cp.Variable(numberOfBuyers)

        # Objective
        obj = cp.Minimize(cp.sum(prices) - budgets.T @ cp.log(betas))

        # Constraints
        constraints = [prices[j] >= cp.multiply(valuations[:,j], betas) for j in range(numberOfGoods)]

        # Convex Program for primal
        dual = cp.Problem(obj, constraints)

        # Solve Program
        dual.solve()  # Returns the optimal value.
        print("Dual Status (Price): ", dual.status)
        print("Optimal Value Dual (Price): ", dual.value)
        print("Optimal Prices", prices.value)
