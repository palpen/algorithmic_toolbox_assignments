# Uses python3

import sys


def selection_sort(a):

    for i in range(len(a)):

        minIndex = i

        # find min value in remaining elements of a
        for j in range(i + 1, len(a)):

            if a[j] < a[minIndex]:

                minIndex = j

        # swap a[i] with a[minIndex]
        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp

    return a


if __name__ == '__main__':

    # submission
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(a)
    print(selection_sort(a))
