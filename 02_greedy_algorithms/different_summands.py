# Uses python3

"""
Note: careful about variables in the while condition that reference a value that is changing during the iteration

safe move: among top k, last one gets 1 candy
running time: ?
"""

import sys


def optimal_summands(n):

    summands = []

    i = 0
    sum_summands = 0
    summand_index = 0

    total_n = n

    while sum_summands < total_n:

        i += 1

        if n <= 2 * i:

            summands.append(n)

            return summands

        n -= i

        summands.append(i)

        sum_summands += summands[summand_index]

        summand_index += 1

    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
