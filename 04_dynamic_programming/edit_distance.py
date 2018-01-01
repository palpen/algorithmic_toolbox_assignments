# Uses python3

import numpy as np


def edit_distance(s, t):
    # write your code here

    # length of string s and string t
    n = len(s)
    m = len(t)

    # initialize D with NaN
    D = np.empty([n + 1, m + 1])
    D[:] = np.NAN

    # initialize zeroth row and columns
    for i in range(n + 1):
        D[i, 0] = i

    for j in range(m + 1):
        D[0, j] = j

    # print(D)

    # insertion, deletion, match, mismatch
    # note: start at 1 to skip initialized values
    for j in range(1, m + 1):

        for i in range(1, n + 1):

            # this where the dynamic programming happens (where current value depends on previously recorded values)
            insertion = D[i, j - 1] + 1
            deletion = D[i - 1, j] + 1
            match = D[i - 1, j - 1]
            mismatch = D[i - 1, j - 1] + 1

            # if match, get min of insert, delete, match
            # note: string index starts at 0. Must subtract 1 to match dimension of D.
            if s[i - 1] == t[j - 1]:

                D[i, j] = min(insertion, deletion, match)

            else:

                D[i, j] = min(insertion, deletion, mismatch)

    # print(D)

    return int(D[n, m])


if __name__ == "__main__":
    print(edit_distance(input(), input()))
