import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir) 
sys.path.insert(0,parentdir) 
import numpy as np
from fisher import fisherMarket as m

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
        self.priceHistory = []
        self.priceHistory.append(supplyB)

    def numberOfBuyers(self):
        return self.demandV.shape[0]

    def numberOfGoods(self):
        return self.demandV.shape[1]

    def getPriceHistory(self):
        return self.priceHistory

    def getSupplyV(self):
        return self.supplyV

    def getDemandV(self):
        return self.demandV

    def market(self, supplyB, utilityD, utilityS):

        # Create Supply Side
        supply = m.FisherMarket(V = self.getSupplyV(), B = supplyB)
        supplyD, supplyS = supply.getDS(utilityD) # solve for demand & supply
        X, w = supply.getCache() # store the allocation and wages

        # Create the new demand side market
        demand = m.FisherMarket(self.getDemandV(), supplyD)
        demandD, demandS = demand.getDS(utilityS)  # solve for demand & supply
        Q, p = demand.getCache() # store the allocation and prices

        B = demandS

        return (Q, p, X, w, B)



    def solve(self, epsilon, supplyB, utilityD, utilityS, printResults = False):
        iter = 1
        prevBudgets = np.ones(self.numberOfGoods()) * np.inf
        prevDiff = 100000000
        isNotContraction = -1

        while ((np.sum(np.abs(prevBudgets - supplyB)) > epsilon) and (iter < 200)):
            isNotContraction += ((prevDiff - np.sum(np.abs(prevBudgets - supplyB))) < 0)
            prevBudgets = supplyB
            iter += 1
            Q, p, X, w, B = self.market(supplyB, utilityD, utilityS)
            supplyB = B



            # keep track of iteration and value
            if(iter %5 == 0 and printResults):
                print(f" iter: {iter} - Epsilon = { np.sum(np.abs(prevBudgets -supplyB))}\n")
                print(f"iteration {iter}: \n\twages: {w}\n\tBudgets: {B}")

        if(iter < 200):
            if(printResults):
                print(f"\nMarket converges with iter {iter}- Epsilon = { np.sum(np.abs(prevBudgets - supplyB))}\n")
                print(f"Initial GDP: {np.sum(self.supplyB)}\nGDP (firm budgets): {np.sum(B)}\nGDP (workers' wages): {np.sum(w)}")

            # Check that endowments do not disappear i.e. sum of budgets = sum of wages
            if( (abs((np.sum(B) - np.sum(w))) > np.sum(B)*0.001)):
                print(f"Budgets of firms: {B}\nWages of workers: {w}\nInitial Firm Budgets: {self.supplyB}")
            assert abs(np.sum(B) - np.sum(w)) < np.sum(B)*0.001

        if(isNotContraction):
            print(f"It is not a contraction : isNotContraction value  {isNotContraction}")

        if (printResults):
            print(f"Prices: {p}\nWages: {w}\nBudgets: {B}")

        return (Q, p, X, w, B)
