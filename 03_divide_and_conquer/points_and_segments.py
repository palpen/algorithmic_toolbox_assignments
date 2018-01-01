# Uses python3
# organizing a lottery (advanced problem 5)

"""
Alex hint: For each point xi consider a pair (xi, 'p'). Fore each segment [ai,bi] consider two pairs: (ai, 'l') and (bi, 'r') (p, l, r stand for point, left, and right, respectively). This gives you p+2s pairs. Define an order on such pairs and sort the pairs with respect to this order.


2 3
0 5
7 10
1 6 11

1 3
-10 10
-100 100 0

3 2
0 5
-3 2
7 10
1 6

2 3
0 100
7 7
1 6 11

3 3
8 11
9 11
12 14
11 11 12
"""

import sys


def fast_count_segments(starts, ends, points):

    cnt = [0] * len(points)
    a_tuple = []

    # 1: place starts, ends, and points into a list of tuples
    for i in range(len(starts)):

        tupL = tuple([starts[i], "L{0}".format(i)])
        tupR = tuple([ends[i], "R{0}".format(i)])

        a_tuple.append(tupL)
        a_tuple.append(tupR)

    for i in range(len(points)):

        tupP = tuple([points[i], "P{0}".format(i)])

        a_tuple.append(tupP)

    # print(a_tuple)

    # 2: sort the segments by left most end points
    # ensures sort by second element of tuple also (deals with cases where a segment endpoint is same value as point resulting in their ordering in a_tuple_s being incorrect)
    a_tuple_s = sorted(a_tuple)

    # 3: count num segments spanning each point
    # L_counter = [0] * len(starts)
    L_counter = 0

    for i in range(len(a_tuple_s)):

        # left endpoint of segment
        if a_tuple_s[i][1][0] == 'L':

            L_counter += 1

        # point
        elif a_tuple_s[i][1][0] == 'P':

            # get index number from a_tuple_s[i][1]
            p_index = a_tuple_s[i][1][1:]

            cnt[int(p_index)] = L_counter

        # right endpoint of segment (reduce L_counter to remove segment from count for next points in iteration)
        else:

            L_counter -= 1

    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':

    # submission #
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')

    # testing #
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # m = data[1]
    # starts = data[2:2 * n + 2:2]
    # ends = data[3:2 * n + 2:2]
    # points = data[2 * n + 2:]

    # print("num segments: {0}, num points: {1}".format(n, m))
    # print("segment left points: {0}".format(starts))
    # print("segment right points: {0}".format(ends))
    # print("points: {0}".format(points))

    # print("")
    # print("results:")

    # print("")
    # print("fast result: {0}".format(fast_count_segments(starts, ends, points)))
    # print("naive result: {0}".format(naive_count_segments(starts, ends, points)))

    # testing 2
    # a = [(0, 'L0'), (100, 'R0'), (7, 'L1'), (7, 'R1'), (1, 'P0'), (6, 'P1'), (11, 'P2')]
    # print(sorted(a))