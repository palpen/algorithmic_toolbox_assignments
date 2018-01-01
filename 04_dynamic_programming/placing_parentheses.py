# Uses python3

import numpy as np


def evalt(a, b, op):
    """
    given digits a and digit b and operation op, return (a op b)
    """
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def minmax(i, j, M, m, operations):
    """
    Calculate the minimum and maximum value of subexpression i,j

    input:
    - i, j (index to get subset of an expression)
    - M, m (table containing maximum and minimum values of each subexpressions)
    - operations (list containing set of all the operations in the input expression)

    output:
    - max and min values of subexpression i,j

    note:
    - a expression is defined by a sequence of integers and operations
    - 5 * 3 + 4 - 7 is one such expression, where in the list of digits [5, 3, 4, 7], i = 0 and j = 3 (corresponding to the digits 5 and 7, respectively)
    - one subexpression of this expression is 3 + 4
        - in this case, i = 1, j = 2
        - the operation governing this subexpression is just +, which is the j = j - 1 = 2 - 1 in the list of operations [*, +, -]
    """

    minval = float('inf')
    maxval = float('-inf')

    for k in range(i, (j - 1) + 1):

        # print("   operation: {0}".format(operations[k]))
        a = evalt(M[i, k], M[k + 1, j], operations[k])
        b = evalt(M[i, k], m[k + 1, j], operations[k])
        c = evalt(m[i, k], M[k + 1, j], operations[k])
        d = evalt(m[i, k], m[k + 1, j], operations[k])

        # print("a: {0}, b: {1}, c: {2}, d: {3}".format(a, b, c, d))

        minval = min(minval, a, b, c, d)
        maxval = max(maxval, a, b, c, d)

    return (minval, maxval)


def get_maximum_value(dataset):
    """
    Algorithm that uses dynamic programming to get the maximum value that a given expression can attain

    input: a string of an arithmetic expression, such as 5*7+3-4 (valid operations are *, +, and -)
    output: the maximum possible value that can be attained by the arithmetic expression
    """

    # 1. parse input
    # get digits into a list that preserves its order
    # get operations into a list that preserves order

    digits = [int(dataset[i]) for i in range(len(dataset)) if i % 2 == 0]

    operations = [dataset[i] for i in range(len(dataset)) if i % 2 != 0]

    n = len(digits)

    # 2. initialize min and max arrays
    m = np.zeros([n, n])
    M = np.zeros([n, n])

    # 3. initialize diagonal elements of each array
    # subexpressions that contain only one integer
    for i in range(n):

        m[i, i] = digits[i]
        M[i, i] = digits[i]

    # 4. iterate along top half of diagonal
    # each cell is the min or max value of subexpression i to j
    # min and max value of a given subexpression is calculated in the minmax() function
    for s in range(1, (n - 1) + 1):

        for i in range(n - s):

            j = i + s

            m[i, j], M[i, j] = minmax(i, j, M, m, operations)

    return int(M[0, -1])


if __name__ == "__main__":
    print(get_maximum_value(input()))

    # print(minmax(1,1))
