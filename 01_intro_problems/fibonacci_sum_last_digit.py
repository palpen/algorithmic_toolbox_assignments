# Uses python3

"""
To solve this, use the combinatoric identity of a sum of a sequence of Fibonacci. Then, use the Pisano period to reduce the evaluation of a Fibonacci number to a smaller and more easily calculable one.
"""

import sys


def fibonacci(n):

    fib_array = []

    fib_array.insert(0, 0)
    fib_array.insert(1, 1)

    for i in range(2, n + 1):

        last2sum = fib_array[i - 1] + fib_array[i - 2]
        fib_array.insert(i, last2sum)

    return fib_array[n]


def pisano_period_length(m):

    # calculate the length of the pisano period of F_i mod m
    # the *trick* is that for a given m:
    # fib(i) % m = (fib(i-1) % m + fib(i-2) % m) % m

    i = 2

    pisano_val_mod_current = 1
    pisano_val_mod_prev = 0

    while True:

        pisano_val_mod_i = (pisano_val_mod_prev + pisano_val_mod_current) % m

        # check if reached start of new pisano period
        if pisano_val_mod_current == 0 and pisano_val_mod_i == 1:

            pisano_length = i - 1

            break

        pisano_val_mod_prev = pisano_val_mod_current
        pisano_val_mod_current = pisano_val_mod_i

        i += 1

    return pisano_length


def fibonacci_sum_fast(n):

    # Sum of n Fibonacci numbers (see Fibonnaci wikipedia entry)
    # sum of n Fib. num. = fibonacci(n + 2) - 1

    remainder_n_mod_period_length = (n + 2) % pisano_period_length(10)

    return (fibonacci(remainder_n_mod_period_length) - 1) % 10


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    # calculate fibonnaci and sum them
    for _ in range(n - 1):

        # print(current)
        temp_current = previous + current
        previous = current
        current = temp_current

        sum += current

    # print(sum)
    return sum % 10


if __name__ == '__main__':

    # for submission #
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_fast(n))

    # for testing #
    # i = 10**6
    # print("fast: %d" % (fibonacci_sum_fast(i)))
    # print("fast: %d" % (fibonacci_sum_naive(i)))
    # print("fibnum: %d" % (fibonacci(i)))

    # for i in range(50):

    #     print("fast: %d" % (fibonacci_sum_fast(i)))
    #     print("naive: %d" % (fibonacci_sum_naive(i)))
    #     print("")
