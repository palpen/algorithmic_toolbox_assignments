# Uses python3

"""
To solve it, sort list a, then sort list b, then take the products of each element with the same index. Take the sum of these products.
safe move: highest profit ad x highest avg. click per day slot
runtime: O(nlog(n)) (sorting O(nlog(n)), iteration across n items O(n))
"""

import sys


def max_dot_product(a, b):
    # write your code here
    res = 0

    # sort descending
    a.sort(reverse=True)
    b.sort(reverse=True)

    for i in range(len(a)):
        res += a[i] * b[i]
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
