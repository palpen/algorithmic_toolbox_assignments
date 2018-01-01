# Uses python3
"""
To solve, sort coin denomination in descending order in list coins. Loop through this coin list and check if, for given denomination, the interger m can be divided by coin, c. If it can, give all change in coin, c. Otherwise, give as much of c as change then set m to the remainder and check in next iteration if can give all change in the next denomination. Keep going until all coins are checked.

safe move:
runtime: sort O(nlog(n)),
"""

import sys


def get_change(m):
    # write your code here

    # change is 1, 5, or 10 (note: already sorted---runtime for sort is O(nlog(n))
    coins = [10, 5, 1]

    total_change = 0

    for c in coins:

        m_mod_c = m % c

        if m_mod_c == 0:

            total_change += m // c

            return total_change

        elif m_mod_c > 0:

            total_change += (m - m_mod_c) // c

            m = m_mod_c

    return total_change


if __name__ == '__main__':

    # submission #
    m = int(sys.stdin.read())
    print(get_change(m))

    # testing #
    # m =10
    # print(get_change(m))
