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
        supply = m.FisherMarket(V = self.supplyV, B = self.supplyB)
        prevBudgets = np.ones(supply.numberOfBuyers()) * np.inf
        prevDiff = 100000000
        isNotContraction = -1


        while ((np.sum(np.abs(prevBudgets - supply.getBudgets())) > epsilon) and (iter < 500)):
            # Increment variable if change this time period is bigger than last one
            isNotContraction += ((prevDiff - np.sum(np.abs(prevBudgets - supply.getBudgets()))) < 0)
            prevDiff = np.sum(np.abs(prevBudgets - supply.getBudgets()))

            # keep track of iteration and value
            if(iter %5 == 0):
                print(f" iter: {iter} - Epsilon = { np.sum(np.abs(prevBudgets - supply.getBudgets()))}\n")
                print(f"iteration {iter}: \n\twages: {w}\n\tBudgets: {B}")

            iter += 1

            # Store previous iteration's budgets
            prevBudgets = supply.getBudgets()
            supplyD, supplyS = supply.getDS(utilities) # solve for demand & supply

            # NOTE Above check is taken out because when budgets are not spend entirely, there are then issues.
            # if( abs(np.sum(supplyD)- np.sum(self.supplyB)) >= np.sum(supplyD)*0.001):
            #     print(f"Sum of Supply: {np.sum(supplyD)}\nSum of Budgets: {np.sum(self.supplyB)}")
            # assert abs(np.sum(supplyD)- np.sum(self.supplyB)) < np.sum(supplyD)*0.001


            X, w = supply.getCache() # store the allocation

            # Create the new demand side market
            demand = m.FisherMarket(self.demandV, supplyD)
            demandD, demandS = demand.getDS(utilities)  #solve for demand & supply

            if(np.sum(demandD - self.supplyB) > np.sum(demandD)*0.001):
                print(f"Demand vector {demandD}\nBudget Vector: {self.supplyB}")
            assert np.sum(demandD - self.supplyB) < np.sum(demandD)*0.001


            # Create the newsupply side of the market
            supply = m.FisherMarket(self.supplyV, demandD)

            Q, p = demand.getCache()
            B = supply.getBudgets()


        if(iter < 200):
            print(f"\nMarket converges with iter {iter}- Epsilon = { np.sum(np.abs(prevBudgets - supply.getBudgets()))}\n")

            # Check that endowments do not disappear i.e. inputs = outputs
            if( (abs((np.sum(B) - np.sum(w))) > np.sum(B)*0.001)):
                #or ((np.sum(B) - np.sum(self.supplyB) ) > np.sum(B)*0.001)):
                print(f"Budgets of firms: {B}\nWages of workers: {w}\nInitial Firm Budgets: {self.supplyB}")
            assert abs(np.sum(B) - np.sum(w)) < np.sum(B)*0.001

            # Note below assert is checked because budgets are sometimes not spent.
            #assert abs(np.sum(B) - np.sum(self.supplyB)) < np.sum(B)*0.001

            # Check equilibrium condition that demand side demand is equal to supply side demand
            if(np.sum(np.abs(demandD - demandS)) > np.sum(demandD)*0.001):
                print(f"Supply side Demand: {demandD}\nDemand side Demand: {demandS}")
            assert np.sum(np.abs(demandD - demandS)) < np.sum(demandD)*0.001

            print(f"Initial GDP: {np.sum(self.supplyB)}\nGDP (firm budgets): {np.sum(B)}\nGDP (workers' wages): {np.sum(w)}")

        if(isNotContraction):
            print(f"It is not a contraction : isNotContraction value  {isNotContraction}")



        print(f"Prices: {p}\nWages: {w}\nBudgets: {B}")
        return (X, p, Q, w, B)
