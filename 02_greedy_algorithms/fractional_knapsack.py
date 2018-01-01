# Uses python3
"""
To solve this, sort value / weight first making sure that the index in this sorted list is consistent with the index in the value and weights list (use zip). Then, iterate through sorted list, check if pack still has capacity. If not, then return total value. Otherwise, fill bag with as much of the item i as possible (which should have the highest v/w because the value per weight list has been sorted in descending order). Add value of the amount of item i to total value. Repeat until all items are exhausted.

safe move: take as much of the highest v/w item first
runtime: sort O(nlog(n))? (sort on zipped values sorts on first element of each tuple only)
"""

import sys


def get_optimal_value(capacity, weights, values):

    value = 0

    # calculate value / weight and sort in descending order (also sort weights and values so item index after sort is consistent across each list)
    value_per_weight = [v / w for v, w in zip(values, weights)]

    # print(value_per_weight)

    w_v_vperw = zip(value_per_weight, weights, values)
    w_v_vperw = list(w_v_vperw)
    w_v_vperw.sort(reverse=True)

    # print(w_v_vperw)

    # iterate through sorted items
    for i in range(len(w_v_vperw)):

        if capacity == 0:

            return value

        w = w_v_vperw[i][1]
        a = min(w, capacity)

        vperw = w_v_vperw[i][0]
        value += a * vperw  # recover value of item i

        w -= a

        capacity -= a

    return value


if __name__ == "__main__":

    # submission #
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.05f}".format(opt_value))

    # testing #
    # python3 ../../test_generator.py; python3 fractional_knapsack.py < input_vals.txt
