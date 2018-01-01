# Uses python3

"""
count number of inversions in list. To solve this, implement a modified version of the merge sort algorithm. The trick is explained in the merge function used in the merge sort algorithm
"""

import sys
import random


def merge(b, c):
    """
    merge function used in mergeSort

    """
    D = []
    b_gr_c_counter = 0

    while b != [] and c != []:

        b_first = b[0]
        c_first = c[0]

        if b_first <= c_first:

            D.append(b_first)
            del b[0]

        elif b_first > c_first:

            D.append(c_first)
            del c[0]

            # this is the TRICK---if i in b is greater than j in c, then all i+1, i+2 is also greater than j because b is sorted in ascending order
            b_gr_c_counter += len(b)

    # append rest of elements in b or c
    D.extend(b)
    D.extend(c)

    return [D, b_gr_c_counter]


def number_of_inversions(a):
    """
    implement the merge sort algorithm
    """

    if len(a) == 1:

        return [a, 0]

    m = len(a) // 2

    b, num_inv_b = number_of_inversions(a[0:m])

    c, num_inv_c = number_of_inversions(a[m:len(a)])

    # accumulate num of inversions from recursive calls
    total_num_inv = num_inv_b + num_inv_c

    # merge b and c and count the number of inversions for their combination
    a_merged, num_inv = merge(b, c)

    total_num_inv += num_inv

    # print(number_of_inversions)

    return [a_merged, total_num_inv]


def naive_number_of_inversions(a):
    """
    naive implementation of algorithm
    """

    num_inv = 0

    for i in range(len(a)):

        for j in range(i + 1, len(a)):

            if a[i] > a[j]:

                num_inv += 1

    return num_inv


if __name__ == '__main__':

    # submission #
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(number_of_inversions(a)[1])

    # testing #
    # print(get_number_of_inversions(a, b, 0, len(a)))

    # a = [7, 1, 7, 1]
    # b = [7, 3]
    # c = [1, 5]

    # print(number_of_inversions(a))

    # stress testing

    # for _ in range(1000):

    #     a = random.sample(range(1, 100), 4)

    #     print(a)

    #     quick = number_of_inversions(a)[1]
    #     naive = naive_number_of_inversions(a)

    #     print("{2} | quick: {0}, naive: {1}".format(quick, naive, a))

    #     assert(quick == naive)


    # print(number_of_inversions(a)[1])
    # print(naive_number_of_inversions(a))
