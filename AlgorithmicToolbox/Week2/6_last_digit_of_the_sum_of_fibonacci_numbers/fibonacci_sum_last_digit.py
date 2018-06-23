# Uses python3
# Calculate the last digit of the sum of the first n fibonacci numbers
# Note that the sum of n fibonacci numbers is equal to F(n+2) - 1
# The last digit of a number is the number mod 10
# Note the pisano period for mod 10 is 60.
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    fsum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        fsum += current

    return fsum % 10

def fibonacci_sum(n):
    if n <= 1:
        return n

    fib_reference = get_fibonacci_huge_last_digit(n+2)
    if fib_reference == 0:
        fib_reference += 10
    return fib_reference - 1


def get_fibonacci_huge_last_digit(n):
    if n <= 1:
        return n

    pisano_period = 60
    equivalent_n = n % pisano_period

    previous = 0
    current  = 1

    for _ in range(equivalent_n - 1):
        previous, current = current, previous + current

    return current % 10


if __name__ == '__main__':
    n = int(input())
    # print(fibonacci_sum_naive(n))
    print(fibonacci_sum(n))

    # for n1 in range(n):
    #     expected = fibonacci_sum_naive(n1)
    #     actual = fibonacci_sum(n1)
    #     if actual != expected:
    #         print("Wrong answer: n={}, expected:{}, actual:{}".format(n1, actual, expected))
        # else:
        #     print(actual)