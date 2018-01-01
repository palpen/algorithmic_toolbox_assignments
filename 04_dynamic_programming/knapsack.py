# Uses python3
import sys
import numpy as np
import itertools
import bisect
import random


def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result


def slow_knapsack_wo_rep(W, wt):
    """
    Slow implementation of the knapsack without replacement algorithm. Takes all combinations of list of weights, wt, sum each of them, and take the maxium that is less than the knapsack weight, W.

    input:
    W: knapsack capacity
    wt: list containing the weights of each pieces of gold

    output:
    maximum weigt of gold that can fit in the knapsack with capacity, W.
    """

    combs = []

    # create all possible combinations of items in list wt (O(2^n))
    for i in range(len(wt) + 1):

        num_combs = [list(x) for x in itertools.combinations(wt, i)]
        combs.extend(num_combs)

    # get sum of items in each combination in combs and sort them
    combs_sum = [sum(x) for x in combs]
    combs_sum.sort()

    # locate insertion point for W that preserves sorted order of combs_sum
    index = bisect.bisect(combs_sum, W)

    # return
    return combs_sum[index - 1]


def fast_knapsack_wo_rep(W, wt):
    """
    Fast implementation of knapsack without replacement using dynamic programming.

    input:
    W: knapsack capacity
    wt: list containing the weights of each pieces of gold

    output:
    maximum weigt of gold that can fit in the knapsack with capacity, W.

    note:
    - value of item i is just its weight (8kg => value 8)
    """

    num_items = len(wt) + 1  # incld zero

    # initialize max val array
    value = np.zeros([num_items, W + 1])

    # dynamic programming
    for i in range(1, num_items):

        for w in range(1, W + 1):

            # previous maximum value with max weight w does not use item i
            value[i, w] = value[i - 1, w]

            # a subproblem where item i is used cannot be optimal if item i's weight exceeds the limit, w. This if condition ensures that item i's weight is less than max weight of w.
            if wt[i - 1] <= w:

                val = value[i - 1, w - wt[i - 1]] + wt[i - 1]

                if value[i, w] < val:

                    value[i, w] = val

    return int(value[num_items - 1, W])


if __name__ == '__main__':

    # submission
    input = sys.stdin.read()
    W, n, *wt = list(map(int, input.split()))
    print(fast_knapsack_wo_rep(W, wt))

    # testing
    # stress testing
    # for _ in range(1000):
    #     W = random.randint(1, 100)

    #     # create random lenght of list
    #     n = random.randint(1, 15)
    #     wt = [random.randint(0, 450) for _ in range(n)]

    #     print("knapsack capacity: {0}".format(W))
    #     print("lightest item in wt: {0}".format(min(wt)))

    #     print("fast result: max gold carried = {0}".format(fast_knapsack_wo_rep(W, wt)))
    #     print("slow result: max gold carried = {0}".format(slow_knapsack_wo_rep(W, wt)))
    #     assert fast_knapsack_wo_rep(W, wt) == slow_knapsack_wo_rep(W, wt)
    #     print("")

