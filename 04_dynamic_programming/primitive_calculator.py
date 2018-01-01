# Uses python3

"""
This problem is similar to the change problem. Suppose n = 6. In dynamic programming problems, instead of solving the problem from right to left ()

TODO !!!
- explain algorithm (look at scratch paper)
- implement code that outputs intermediate steps

failing test case
11809
correct: 1 3 9 27 81 82  164 328 656 1312 3936 11808 11809 (12 operations)
gives:   1 3 9 27 81 243 244 245 246 492  984  1968  3936 11808 11809 (14 operations)
- fixed it by making mod2== 0 come before the mod3 == 0 if condtion (!!!)

"""

import sys


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def primitive_calculator(n):
    """
    input: integer, n
    output: list containing minimum number of operations for 1,...,n

    # MNO = Minimum Number of Operations
    index:   0  1  2  3  4  5  6
    integer: 1  2  3  4  5  6  7
    MNO:     0  1  1  2  3  2  3
    """

    # for n == 1 (corresponding to index 0 in MNO list), MNO is always 0
    MNO = [0]

    for i in range(2, n + 1):   # we skip 1 because MNO is always 0 for n == 1
        # note: indexing starts at 0, hence i-1 for result corresponding to integer i

        mod3 = i % 3
        mod2 = i % 2

        if mod3 != 0 and mod2 != 0:
            # if integer is not divisible by 3 or 2, result is previous result plus 1 operation (which is the add 1 operation)

            MNO.append(MNO[i - 2] + 1)

        elif mod3 != 0 and mod2 == 0:
            # divisible by 2 but not 3

            previous_cell = MNO[i - 2]

            idiv2 = i // 2
            mno_i_div_2 = MNO[idiv2 - 1]

            MNO.append(min(previous_cell, mno_i_div_2) + 1)

        else:
            # if divisible by 3, but not two, them minimum of {previous operation plus 1 operation, MNO for integer / 3 plus 1 operation}

            previous_cell = MNO[i - 2]

            idiv3 = i // 3
            mno_i_div_3 = MNO[(idiv3) - 1]

            MNO.append(min(previous_cell, mno_i_div_3) + 1)

    return MNO


def primitive_calculation_output(n, MNO):
    """
    Returns the sequence of intermediate values leading to integer n

    input: n = integer, MNO = list containing min operations for each integer 1,...,n
    output: list containing intermediate values

    e.g. for n = 5, intermediate values are 1,2,4,5

    Note: index starts at 0 and does not correspond to integer values
    """

    p = []

    if n == 0 or n == 1:

        return [1]

    if n > 0 and MNO[n - 1] == MNO[n - 2] + 1:
        # plus 1 operation: current MNO value comes from previous MNO value plus 1 operation

        pco = primitive_calculation_output(n - 1, MNO[:n - 1])

        return pco + [n]

    elif n > 0 and MNO[n - 1] == MNO[n // 3 - 1] + 1:
        # multiply 3 operation: current MNO value comes from an operation where corresponding integer is a multiple of 3

        pco = primitive_calculation_output(n // 3, MNO[:(n // 3)])

        return pco + [n]

    else:
        # multiply 2 operation: current MNO value comes from an operation where corresponding integer is a multiple of 2

        pco = primitive_calculation_output(n // 2, MNO[:(n // 2)])

        return pco + [n]

    return p


if __name__ == '__main__':

    input = sys.stdin.read()
    n = int(input)

    # submission
    MNO = primitive_calculator(n)

    sequence = primitive_calculation_output(n, MNO)
    minnumop = len(sequence) - 1
    print(minnumop)
    for x in sequence:
        print(x, end=' ')

    print("")


    # incorrect solution
    # sequence = list(optimal_sequence(n))
    # print(len(sequence) - 1)
    # for x in sequence:
    #     print(x, end=' ')
