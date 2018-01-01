# Uses python3

"""
Algorithm finds the key x in array a. It does this iteratively by cutting a in half and checking if x is in the middle, above it, or below it. It then proceeds to continue cutting these segments until x has been found

todo: implement it recursively
"""

import sys
import math


def binary_search(a, x):

    # print("searching for {0}".format(x))
    # a is the array containing data, x is the value to search
    low, high = 0, (len(a) - 1)

    while low <= high:

        mid = math.floor(low + (high - low) / 2)
        print("mid: {0}".format(mid))

        if x == a[mid]:

            return mid

        elif x < a[mid]:

            high = mid - 1

        else:

            low = mid + 1

    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':

    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    # print(n)

    m = data[n + 1]
    # print(m)

    a = data[1: n + 1]
    # print(a)

    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        # print("linear: f or x == {0}, index found: {1}".format(x, linear_search(a, x)), end=" ")
        # print("")
        # print("binary: f or x == {0}, index found: {1}".format(x, binary_search(a, x)), end=" ")
        # print("")
        # print("")

        # submission
        print(binary_search(a, x), end=" ")
