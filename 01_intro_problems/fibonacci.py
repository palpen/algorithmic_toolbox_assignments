# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_fast(n):

    fib_array = []

    fib_array.insert(0, 0)
    fib_array.insert(1, 1)

    for i in range(2, n + 1):

        last2sum = fib_array[i - 1] + fib_array[i - 2]
        fib_array.insert(i, last2sum)

    return fib_array[n]


if __name__ == '__main__':

    n = int(input())

    # print("fast fib: %s" % str(calc_fib_fast(n)))
    # print("slow fib: %s" % str(calc_fib(n)))

    print(calc_fib_fast(n))
