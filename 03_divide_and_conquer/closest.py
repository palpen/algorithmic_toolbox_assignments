# Uses python3
# Advanced problem: Finding the closest pair of points

"""
See Cormen, Algorithms pg 1039 for description of algorithm

2
0 0
3 4
ans: 5.0

4
7 7
1 100
4 8
7 7
ans: 0.0

11
4 4
-2 -2
-3 -4
-1 3
2 3
-4 0
1 1
-1 -1
3 -1
-4 2
-2 4
ans: 1.414213

"""

import sys
import math


def euclidean_distance(x1, y1, x2, y2):

    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def minimum_distance(x, y):
    """
    x: list of x coordinates
    y: list of y coordinates

    e.g. [(3,4), (1,3)]
    x = [3, 1]
    y = [4, 3]

    len(x) == len(y)
    """

    # base case
    print("")

    # less then 3 points
    if len(x) <= 3:

        print("Less than 3 points")
        print(x, y)

        eu_dist_3 = []

        for i in range(len(x)):

            for j in range(i + 1, len(x)):

                dist = euclidean_distance(x[i], y[i],
                                          x[j], y[j])

                eu_dist_3.append(dist)

        print(eu_dist_3)

        return min(eu_dist_3)

    # greater than 3 points!!!
    elif len(x) > 3:

        print("Greater than 3")

        # 1: sorting #
        # store in vector pair (x,y) for sorting
        xy_coord = list(zip(x, y))

        # sort by x values and if x's are equal, sort by y
        xy_coord_s = sorted(xy_coord)

        # unpack back to a list
        x = [i[0] for i in xy_coord_s]
        y = [i[1] for i in xy_coord_s]

        # 2: middle point #
        mid = len(x) // 2

        # 3: recursive calls #
        x_left, y_left = x[:mid], y[:mid]
        md1 = minimum_distance(x_left, y_left)

        x_right, y_right = x[mid:], y[mid:]
        md2 = minimum_distance(x_right, y_right)

        delta = min(md1, md2)

        # calculate distance between each point in left and right array !!!

        # TBC: !!!! STOPPED HERE
        # for l in range(len(x_left)):

        #     for r in range(len(x_right)):

        #         dist = euclidean_distance(x_left[l], y_left[l],
        #                                   x_right[r], y_right[r])

        #         if dist == 0:

        #             return 0

        #         elif dist:

        #             pass

        # check between left and right subarrays
        # break right away if distance is zero between any two points in subarray

        print("md1: {0}".format(md1))
        print("md2: {0}".format(md2))

        # print("min(md1, md2) = {0}".format(min(md1, md2)))

        return delta


def naive_minimum_distance(x, y):

    eu_dist = []

    for i in range(len(x)):

        for j in range(i + 1, len(x)):

            eu_dist.append(euclidean_distance(x[i], y[i],
                                              x[j], y[j]))

    print("eu_dist: {0}".format(eu_dist))

    return min(eu_dist)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]

    # submission
    # print("{0:.9f}".format(minimum_distance(x, y)))

    print("fast results: {0}".format(minimum_distance(x, y)))

    print("")

    print("naive results: {0}".format(naive_minimum_distance(x, y)))

    # print(euclidean_distance(7, 7, 1, 100))
    # print(euclidean_distance(2, 2, 1, 100))
    # print(euclidean_distance(7, 7, 2, 2))

