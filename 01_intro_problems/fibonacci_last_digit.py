# Uses python3
# 1. Run
#     python3 APlusB.py
# then enter two numbers and press ctrl-d

import sys


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    # calculate the Fib. numbers given n
    for _ in range(n - 1):
        # print(_)
        previous, current = current, previous + current

        print("prev: %d, curr: %d" % (previous, current))

    return current % 10


def get_fibonacci_last_digit_fast(n):

    fib_array_last_digit = []

    fib_array_last_digit.insert(0, 0)
    fib_array_last_digit.insert(1, 1)

    for i in range(2, n + 1):

        last2sum = fib_array_last_digit[i - 1] + fib_array_last_digit[i - 2]

        # store only last digit of F_i to conserve memory
        fib_array_last_digit.insert(i, last2sum % 10)

    return fib_array_last_digit[n]


if __name__ == '__main__':

    input = sys.stdin.read()
    n = int(input)
    # print(get_fibonacci_last_digit_naive(n))
    print(get_fibonacci_last_digit_fast(n))
