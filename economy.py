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


    def solve(self, epsilon):
        iter = 1
        # Create supply side
        supply = m.FisherMarket(self.supplyV, self.supplyB)
        prevBudgets = np.ones(supply.numberOfBuyers()) * np.inf


        while ((np.sum(np.abs(prevBudgets - supply.getBudgets())) > epsilon) or iter > 200):

            # keep track of iteration and value
            if(iter %10 == 0):
                print(f" iter: {iter} - Epsilon = { np.sum(np.abs(prevBudgets - supply.getBudgets()))}\n")

            iter += 1

            # Store previous iteration's budgets
            prevBudgets = supply.getBudgets()
            D, S = supply.getDS("quasi-linear") # solve for demand & supply

            # Create the new demand side market
            demand = m.FisherMarket(self.demandV, D)
            D, S = demand.getDS("quasi-linear")  #solve for demand & supply

            # Create the newsupply side of the market
            supply = m.FisherMarket(self.supplyV, D)

        print("Market converges")
