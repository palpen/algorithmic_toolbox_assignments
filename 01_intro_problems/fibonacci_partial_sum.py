# Uses python3
import sys
import random

"""
To solve this, take the sum form 0 to m, then calculate the full some from 0 to n. Then subtract the first sum from the second sum (use the combinatoric identity for the sum of a sequence of Fibonacci numbers when taking the difference). Using the combinatoric identities, you'll get

(F_(n+2) - 1) - (F_(m-1+2) - 1) % 10

use mod arithmetic, (a - b) % 10 = (a % 10 - a % 10) % 10 to decompose the expression above. Then, use the Pisano period results to very quickly evaluate F_(n+1) % 10 and F_(m-1+2) % 10 for very large numbers of n and m.
"""


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


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def fibonacci_partial_sum_fast(from_, to):

    # Get last digit of F_m+1
    rem_m_mod_per_length = (from_ + 1) % pisano_period_length(10)
    fib_m_plus_1_last_digit = fibonacci(rem_m_mod_per_length) % 10

    # get last digit of F_n+2
    rem_n_mod_per_length = (to + 2) % pisano_period_length(10)
    fib_n_plus_2_last_digit = fibonacci(rem_n_mod_per_length) % 10

    # (F_n+2 % 10 - F_m+1 % 10) % 10
    last_digit_partial_sum = (fib_n_plus_2_last_digit - fib_m_plus_1_last_digit) % 10

    return last_digit_partial_sum


if __name__ == '__main__':

    # for submission #
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_fast(from_, to))

    # for testing #
    # input_dict = {1: {'m': 0, 'n': 0},
    #               2: {'m': 10, 'n': 10},
    #               3: {'m': 3, 'n': 10},
    #               4: {'m': 0, 'n': 10**14},
    #               5: {'m': 10**14, 'n': 10**14},
    #               6: {'m': 100, 'n': 1000}
    #               }

    # test_case_num = 5

    # print("naive: %d" % (fibonacci_partial_sum_naive(input_dict[test_case_num]['m'], input_dict[test_case_num]['n'])))
    # print("fast: %d" % (fibonacci_partial_sum_fast(input_dict[test_case_num]['m'], input_dict[test_case_num]['n'])))

    # # stress test #
    # while True:

    #     n = random.randint(0, 100)
    #     m = random.randint(0, n)

    #     fast_result = fibonacci_partial_sum_fast(m, n)
    #     naive_result = fibonacci_partial_sum_naive(m, n)

    #     if fast_result == naive_result:
    #         print("OK! m: %d n: %d" % (m, n))

    #     elif fast_result != naive_result:
    #         print("Failed! m: %d n: %d" % (m, n))

    #         break
