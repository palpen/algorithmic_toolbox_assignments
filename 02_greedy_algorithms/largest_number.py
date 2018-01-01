# Uses python3

"""
Trick is in is_greq(.) function. Pairwise comparison must be made appropriately in cases where digits have the same first or second digits

safe move:
runtime:
"""

import sys

# not necessary
# def left_most_digit(x):
#     # get the left most digit of an integer.
#     # Note if first digit of x is 9, it is important for x to be an integer in the while condition, otherwise, when the loop reaches 9.2 for x = 92, it divides this again by 10, resulting in a final value of 0.92 (or int(0.92) = 0)

#     while int(x) > 9:

#         x = x / 10

#     return int(x)


def is_greq(digit, max_digit):
    # evaluate which combination of digit and max_digit results in greater salary. Robust to cases where digits ordering in input matter: 21 2 or 2 21 (where 21 2 results in the correct salary of 221)

    # Intuition: will it result in a bigger number if we do d_md versus md_d? If yes, make digit the new max_digit in line 50 below

    d_md = digit + max_digit

    md_d = max_digit + digit

    return int(d_md) >= int(md_d)


def largest_number(digits):

    salary = ""

    max_digit = "0"

    # print(digits)

    while True:

        for digit in digits:

            if is_greq(digit, max_digit):

                max_digit = digit

        salary += str(max_digit)

        digits.remove(max_digit)

        if len(digits) == 0:

            break

        max_digit = "0"

    return int(salary)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    # print(a)
    salary = largest_number(a)
    print(salary)
    # print(type(salary))
