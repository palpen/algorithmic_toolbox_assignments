# Uses python3
"""
To solve this, avoid calculating fib(i) % m for larger and larger i. Use the fact that
for a given m, fib(i) % m = (fib(i-1) % m + fib(i-2) % m) % m.
"""

import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def fibonacci(n):

    fib_array = []

    fib_array.insert(0, 0)
    fib_array.insert(1, 1)

    for i in range(2, n + 1):

        last2sum = fib_array[i - 1] + fib_array[i - 2]
        fib_array.insert(i, last2sum)

    return fib_array[n]


def pisano_period_length(m):

    # calculate the length of the pisano period corresponding to m
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


def get_fibonacci_huge_fast(n, m):

    remainder_n_mod_period_length = n % pisano_period_length(m)

    return fibonacci(remainder_n_mod_period_length) % m


def mem_use_bytes(tup):

    # usage: memory_usage((func, (x,y,z))), where (x,y,z) contains func's arguements

    from memory_profiler import memory_usage

    mem_use_total_MiB = sum(memory_usage(tup))
    mem_use_total_bytes = (mem_use_total_MiB // 1.04858)

    return mem_use_total_bytes


if __name__ == '__main__':

    # python3 ../../test_generator.py; python3 fibonacci_huge.py < input_vals.txt

    input = sys.stdin.read()
    n, m = map(int, input.split())

    # print(pisano_period_length(m))

    # print(get_fibonacci_huge_naive(n, m))
    # print(mem_use_bytes((get_fibonacci_huge_naive, (n, m))))

    print(get_fibonacci_huge_fast(n, m))
    # print(mem_use_bytes((get_fibonacci_huge_fast, (n, m))))
