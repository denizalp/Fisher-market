import cvxpy as cp


def compute_util_max_bundle(valuation, prices, budget):
    """
    Given a vector of consumer valuations, v, a price vector, p, and a budget, compute the utility
    of a utility-maximizing bundle. Mathematically, solve the linear program:
    max_{x} xv
    s.t. xp <= budget
    :param valuation: a consumer's valuation for goods.
    :param prices: prices of goods.
    :param budget: the consumer's budget
    :return:
    """
    num_items = len(valuation)
    x = cp.Variable(num_items)
    prob = cp.Problem(cp.Maximize(x @ valuation),
                      [x @ prices <= budget,
                       x >= 0])
    prob.solve()
    return prob.value
