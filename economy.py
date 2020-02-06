import numpy as np
import fisherMarket as m

class Economy:
    """A class that models an economy witha  supply and a demand side."

        Attributes:
        supplyV = valuation matrix for firms
        supplyB = vector of budgets for firms
        demandV = valuation matrix for consumers
    """

    def __init__(self, supplyV, supplyB, demandV):
        self.supplyV = supplyV
        self.supplyB = supplyB
        self.demandV = demandV


    def solve(self, epsilon, utilities = "quasi-linear"):
        iter = 1
        # Create supply side
        supply = m.FisherMarket(self.supplyV, self.supplyB)
        prevBudgets = np.ones(supply.numberOfBuyers()) * np.inf
        prevDiff = 100000000
        isNotContraction = -1


        while ((np.sum(np.abs(prevBudgets - supply.getBudgets())) > epsilon) and (iter < 500)):
            # Increment variable if change this time period is bigger than last one
            isNotContraction += ((prevDiff - np.sum(np.abs(prevBudgets - supply.getBudgets()))) < 0)
            prevDiff = np.sum(np.abs(prevBudgets - supply.getBudgets()))

            # keep track of iteration and value
            if(iter %10 == 0):
                print(f" iter: {iter} - Epsilon = { np.sum(np.abs(prevBudgets - supply.getBudgets()))}\n")

            iter += 1

            # Store previous iteration's budgets
            prevBudgets = supply.getBudgets()
            D, S = supply.getDS(utilities) # solve for demand & supply
            X, p = supply.getCache() # store the allocation

            # Create the new demand side market
            demand = m.FisherMarket(self.demandV, D)
            D, S = demand.getDS(utilities)  #solve for demand & supply

            # Create the newsupply side of the market
            supply = m.FisherMarket(self.supplyV, D)

        if(iter < 200):
            print(f"Market converges with iter {iter}- Epsilon = { np.sum(np.abs(prevBudgets - supply.getBudgets()))}\n")


        if(isNotContraction):
            print(f"It is not a contraction : isNotContraction value  {isNotContraction})")
        Q, w = demand.getCache()
        B = supply.getBudgets()

        return (X, p, Q, w, B)
