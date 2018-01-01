# Uses python3

# what are all the integers that are divisible by both a and b? The smalles of these integers is the least common multiple


import sys


def gcd_fast(a, b):

    if b == 0:

        return a

    ab_remain = a % b

    return gcd_fast(b, ab_remain)


def lcm_naive(a, b):

    for l in range(1, a * b + 1):

        if l % a == 0 and l % b == 0:
            return l

    return a * b


def lcm_fast(a, b):

    # uses the fact that lcm(a,b)*gcd(a,b) = a * b
    return (a * b) // gcd_fast(a, b)


def mem_use_bytes(tup):

    from memory_profiler import memory_usage

    mem_use_total_MiB = sum(memory_usage(tup))
    mem_use_total_bytes = mem_use_total_MiB * 1048576

    return mem_use_total_bytes


if __name__ == '__main__':

    input = sys.stdin.read()  # must push control+D to end
    a, b = map(int, input.split())

    print(mem_use_bytes((lcm_naive, (a, b))))
    print(mem_use_bytes((lcm_fast, (a, b))))

    print(lcm_naive(a, b))
    print(lcm_fast(a, b))
