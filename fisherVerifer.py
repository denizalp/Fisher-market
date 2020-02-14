import numpy as np
import cvxpy as cp
import sys
np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

# def verify(X, p, V, b, utility, M = None):
#     """
#     Given and allocation of goods, prices, valuations and utility types, check if
#     a pair of allocation and prices satisfy conditions for a competitive
#     equilibrium, that is 1) supply_j * p_j >= demand_j * p_j and 2) the
#     allocation is envy free.
#
#     Inputs:
#     X : A matrix of allocations (size: |buyers| x |goods|)
#     p : A vector of prices for goods (size: |goods|)
#     V : A matrix of valuations (size: |buyers| x |goods| )
#     b : A vector of budgets (size: |buyers|)
#     utility: The type of utilty function
#     M : Number of goods
#
#     Returns:
#     Boolean: True if (X, p) form a CE for valuations V and budgets b,
#     false otherwise
#     """
#
#     # Check if allocation is envy-free/utility maximizing
#
#     numberOfBuyers, numberOfGoods = V.shape
#
#     # Variables of program
#     alloc = cp.Variable((numberOfBuyers, numberOfGoods))
#
#     # Objective
#     if(utility == "linear"):
#         obj = cp.Maximize(cp.sum(cp.log(cp.sum(cp.multiply(alloc, V), axis = 1))))
#     elif(utility in ["quasilinear", "quasi-linear"] ):
#         obj = cp.Maximize( cp.sum(cp.log( cp.sum( cp.multiply( alloc, (V - np.repeat([p], numberOfBuyers, axis =0) ) ),  axis = 1))))
#
#     else:
#         print(f"Utility function {utility} is invalid")
#         sys.exit()
#
#     # Constraints
#     constraints = [b >= alloc @ p, alloc >= 0, cp.sum(alloc, axis = 0) <=1]
#
#
#     # Convex Program for primal
#     prob = cp.Problem(obj, constraints)
#
#     # Solve Program
#     print(prob.solve())  # Returns the optimal value.
#     print("Status of program: ", prob.status)
#     print(f"Input Allocation: {X}\nVerifier Allocation: {alloc.value}")
#     #return (((X - alloc.value).sum() < 0.01) and (X @ p) )



def verify(X, p, V, b, utility, M = None):
    """
    Given and allocation of goods, prices, valuations and utility types, check if
    a pair of allocation and prices satisfy conditions for a competitive
    equilibrium, that is 1) supply_j * p_j >= demand_j * p_j and 2) the
    allocation is envy free.

    Inputs:
    X : A matrix of allocations (size: |buyers| x |goods|)
    p : A vector of prices for goods (size: |goods|)
    V : A matrix of valuations (size: |buyers| x |goods| )
    b : A vector of budgets (size: |buyers|)
    utility: The type of utilty function
    M : Number of goods

    Returns:
    Boolean: True if (X, p) form a CE for valuations V and budgets b,
    false otherwise
    """
    numberOfBuyers, numberOfGoods = V.shape

    alloc = np.zeros((numberOfBuyers, numberOfGoods))
    for i in range(numberOfBuyers):
        alloc[i,:] = getBuyerBundle(X[i,:], p, V[i,:], b[i], utility)

    print(f"Input Allocation: {X}\nVerifier Allocation: {alloc}")


def getBuyerBundle(x, p, v, b, utility):
    """
    Given prices, valuations and utility types, find the bundle of goods maximize
    the utility of the buyer

    Inputs:
    x : A vector of allocations (size: |buyers| x |goods|)
    p : A vector of prices for goods (size: |goods|)
    v : A vector of valuations (size: |goods| )
    b : A budget (size: |buyers|)
    utility: The type of utilty function

    Returns:
    A vector of allocation for the buyer
    """

    if(utility == "linear"):
        isMaxBundle = True
        for j, price in enumerate(p):
            v[j]/p
    elif(utility in ["quasilinear", "quasi-linear"] ):
        obj = cp.Maximize( alloc.T @ (v - p))

    else:
        print(f"Utility function {utility} is invalid")
        sys.exit()


    # Solve Program
    prob.solve()  # Returns the optimal value.
    return alloc.value
