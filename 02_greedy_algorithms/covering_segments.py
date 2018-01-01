# Uses python3
"""
Problem 4: collecting signatures

To solve:
- first, place a point at the minimum endpoint
    - sort segments by min. end point
- second, check all segments to see if they contain this point
    - if they do, remove these segments from the problem
- update segments set with remainining segments
- repeat (first)
- when segments no longer contain any segment, break (len(segments) == 0)

safe move: place a point at the minimum right most endpoint
runtime: sorting O(nlog(n)), for loop: O(n)
"""

import sys
from collections import namedtuple
from operator import itemgetter

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):

    # segment: list of named tuples
    points = []

    # sort by endpoint
    segments_sorted = sorted(segments, key=itemgetter(1))

    segment_length = len(segments_sorted)

    while segment_length > 0:

        # 1: set point at minimum right most endpoint
        min_right_endpoint = segments_sorted[0].end
        points.append(min_right_endpoint)

        # 2: check all segments to see if it contains min_right_endpoint (remove if it does)
        segments_sorted[:] = [s for s in segments_sorted if not s.start <= min_right_endpoint <= s.end]
        # careful here, the [:] in segments_sorted creates a new list. Bad idea to modify list while iterating over it

        # 3: update new length of segment list
        segment_length = len(segments_sorted)

    return points


if __name__ == '__main__':
    input = sys.stdin.read()

    # turn every value into an integer, then unpack
    n, *data = map(int, input.split())
    # n, *data = input.split()

    # print(data[::2])
    # print(data[1::2])
    segments = list(map(lambda x: Segment(
        x[0], x[1]), zip(data[::2], data[1::2])))

    # print(segments)
    # segments_sorted = sorted(segments, key=itemgetter(1))
    # print(segments_sorted)
    # print(segments[0])
    # print("start: %d end: %d" % (segments[0].start, segments[0].end))

    points = optimal_points(segments)
    print(len(points))

    # print("points length: %s" % (len(points)))
    # print(points)

    for p in points:
        print(p, end=' ')

    # print("")
