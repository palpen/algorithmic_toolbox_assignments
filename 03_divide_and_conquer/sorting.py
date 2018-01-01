# Uses python3
import sys
import random


def partition3(a, l, r):
    """
    Dijkstra's 3-way partitioning algorithm. Partitions array such that the pivot and its copies are in the middle, everything less than pivot is to its left, everything greater than the pivot is to its right.
    """

    if r <= l:

        return

    x = a[l]  # pivot

    lt = l
    gt = r
    i = l

    while i <= gt:  # originall i != gt, which is wrong because i should never be greater than gt

        if a[i] < x:

            a[lt], a[i] = a[i], a[lt]

            lt += 1
            i += 1

        elif a[i] > x:

            a[gt], a[i] = a[i], a[gt]

            gt -= 1

        elif a[i] == x:

            i += 1

    return [lt, gt]


def randomized_quick_sort_3part(a, l, r):

    if l >= r:
        return
    k = random.randint(l, r)
    # k =
    # print("a BEFORE partition: {0}, pivot and index: {1}, {2}".format(a, a[k], k))
    a[l], a[k] = a[k], a[l]  # swap to put a[k] at start of array a. Partition below with respect to this randomly chosen value.

    m1, m2 = partition3(a, l, r)
    # print("a AFTER partition: {0}, m1: {1}, m2: {2}".format(a, m1, m2))
    randomized_quick_sort_3part(a, l, m1 - 1)
    randomized_quick_sort_3part(a, m2 + 1, r)


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]  # swap
    a[l], a[j] = a[j], a[l]  # final swap
    return j


def randomized_quick_sort(a, l, r):

    if l >= r:
        return
    k = random.randint(l, r)
    print("a BEFORE partition: {0}, pivot: {1}".format(a, a[k]))
    a[l], a[k] = a[k], a[l]  # swap to put a[k] at start of array a. Partition below with respect to this randomly chosen value.


    m = partition2(a, l, r)
    print("a AFTER partition: {0}, m: {1}".format(a, m))
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, m + 1, r)


if __name__ == '__main__':

    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    # for submission
    randomized_quick_sort_3part(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

    # for testing
    # b = a[:]

    # print("2-way partition:")
    # randomized_quick_sort(b, 0, n - 1)
    # print("final answer:")
    # for x in b:
    #     print(x, end=' ')

    # print("")
    # print("")

    # print("3-way partition:")
    # randomized_quick_sort_3part(a, 0, n - 1)
    # print("final answer:")
    # for x in a:
    #     print(x, end=' ')

    # print("")
    # print("")  # remove in submission !!
