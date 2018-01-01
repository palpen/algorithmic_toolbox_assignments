# Uses python3
"""
The naive algorithm requires checking for each element if that element is the majority element. It requires a nested for loop. First, loop to pick a given element. Second loop to iterate through entire array to scan and update a counter for every element in array matching the element in the outer for loop. Runtime is O(n^2).

The divide and conquer algorithm reduces the number of elements we have to check.

source: https://stackoverflow.com/questions/36906043/majority-element-python

Some diagrams to help with intuition

input:
5
6 2 2

==NEW RECURSIVE CALL==
list to process: [6, 2, 2]
1: split list: [6, 2, 2]
2: recursive call on a_L: [6] and a_R: [2, 2]

    ==NEW RECURSIVE CALL==
    list to process: [6]
    singleton list: 6

2a: got M_L: 6 from recursive calls

    ==NEW RECURSIVE CALL==
    list to process: [2, 2]
    1: split list: [2, 2]
    2: recursive call on a_L: [2] and a_R: [2]

        ==NEW RECURSIVE CALL==
        list to process: [2]
        singleton list: 2

    2a: get M_L: 2 from recursive calls

        ==NEW RECURSIVE CALL==
        list to process: [2]
        singleton list: 2

    2b: get M_R: 2 from recursive calls

    3: count if M_L: 2 and M_R: 2 are majority
    Return result---majority element in [2, 2] is : 2 (M_L)

2b: got M_R: 2 from recursive calls

3: count if M_L: 6 and M_R: 2 are majority
Return result---majority element in [6, 2, 2] is : 2 (M_R)


input:
5
6 2 2 6 6

==NEW RECURSIVE CALL==
list to process: [6, 2, 2, 6, 6]
1: split list: [6, 2, 2, 6, 6]
2: recursive call on a_L: [6, 2] and a_R: [2, 6, 6]

    ==NEW RECURSIVE CALL==
    list to process: [6, 2]
    1: split list: [6, 2]
    2: recursive call on a_L: [6] and a_R: [2]

        ==NEW RECURSIVE CALL==
        list to process: [6]
        singleton list: 6

    2a: get M_L: 6 from recursive calls

        ==NEW RECURSIVE CALL==
        list to process: [2]
        singleton list: 2

    2b: get M_R: 2 from recursive calls

    3: count if M_L: 6 and M_R: 2 are majority

2a: get M_L: -1 from recursive calls

    ==NEW RECURSIVE CALL==
    list to process: [2, 6, 6]
    1: split list: [2, 6, 6]
    2: recursive call on a_L: [2] and a_R: [6, 6]

        ==NEW RECURSIVE CALL==
        list to process: [2]
        singleton list: 2

    2a: get M_L: 2 from recursive calls

        ==NEW RECURSIVE CALL==
        list to process: [6, 6]
        1: split list: [6, 6]
        2: recursive call on a_L: [6] and a_R: [6]

            ==NEW RECURSIVE CALL==
            list to process: [6]
            singleton list: 6

        2a: get M_L: 6 from recursive calls

            ==NEW RECURSIVE CALL==
            list to process: [6]
            singleton list: 6

        2b: get M_R: 6 from recursive calls

        3: count if M_L: 6 and M_R: 6 are majority

        Return result---majority element in [6, 6] is : 6 (M_L)

    2b: get M_R: 6 from recursive calls

    3: count if M_L: 2 and M_R: 6 are majority
    Return result---majority element in [2, 6, 6] is : 6 (M_R)

2b: get M_R: 6 from recursive calls

3: count if M_L: -1 and M_R: 6 are majority
Return result---majority element in [6, 2, 2, 6, 6] is : 6 (M_R)

"""

import sys
import math


def get_majority_element(a, left, right):

    print("")
    print("==NEW RECURSIVE CALL==")
    print("list to process: {0}".format(a))

    if left == right:
        # empty list
        print("empty list")
        return -1

    if len(a) == 1:
        # singleton list (n == right ==1 ). Return single element
        print("singleton list: {0}".format(a[left]))
        return a[left]

    # 1: split list into two
    print("1: split list: {0}".format(a))

    mid = math.floor(len(a) / 2)
    a_L = a[left:mid]
    a_R = a[mid:right]

    # 2: recursive call on a_L and a_R
    print("2: recursive call on a_L: {0} and a_R: {1}".format(a_L, a_R))
    M_L = get_majority_element(a_L, 0, len(a_L))
    print("2a: got M_L: {0} from recursive calls".format(M_L))

    M_R = get_majority_element(a_R, 0, len(a_R))
    print("2b: got M_R: {0} from recursive calls".format(M_R))

    # 3:
    print("")
    # is M_L and M_R majority?
    count_L = 0
    count_R = 0

    # why search from left to right ???
    print("3: count if M_L: {0} and M_R: {1} are majority".format(M_L, M_R))

    for i in range(left, right):

        if M_L == a[i]:

            count_L += 1

        if M_R == a[i]:

            count_R += 1

    if count_L > math.floor(len(a) / 2):

        print("Return result---majority element in {1} is : {0} (M_L)".format(M_L, a))
        return M_L

    elif count_R > math.floor(len(a) / 2):

        print("Return result---majority element in {1} is : {0} (M_R)".format(M_R, a))
        return M_R

    return -1


if __name__ == '__main__':

    # submission
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    get_majority_element(a, 0, n)
    # if get_majority_element(a, 0, n) != -1:
    #     print(1)
    # else:
    #     print(0)
