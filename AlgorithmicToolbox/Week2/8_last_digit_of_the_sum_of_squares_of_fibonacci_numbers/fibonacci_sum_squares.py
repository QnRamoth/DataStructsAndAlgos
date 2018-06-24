# Uses python3
# Calculates the last digit of the sum of squares of the first n fibonacci numbers.
# Note that the geometric aggregation of successive squares yields a rectangle
# with sides of length F(n) by F(n+1)
# Note also that the last digit of the product of two numbers is equal to
# the last digit of the product of the last digits of those two numbers.
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def fibonacci_sum_squares(n):
    fib_nLastDigit, fib_nPlusOneLastDigit = get_fibonacci_huge_last_digits(n+1)
    return (fib_nLastDigit * fib_nPlusOneLastDigit) % 10

def get_fibonacci_huge_last_digits(n):
    pisano_period = 60
    equivalent_n = n % pisano_period

    previous = 0
    current  = 0

    if equivalent_n == 0:
        return previous,current
    current += 1
    if equivalent_n == 1:
        return previous,current

    for _ in range(equivalent_n - 1):
        previous, current = current, previous + current

    return (previous % 10, current % 10)

if __name__ == '__main__':
    n = int(input())
    # print(fibonacci_sum_squares_naive(n))
    print(fibonacci_sum_squares(n))

    # for n1 in range(n):
    #     expected = fibonacci_sum_squares_naive(n1)
    #     actual = fibonacci_sum_squares(n1)
    #     if actual != expected:
    #         print("Wrong answer: n={}, expected:{}, actual:{}".format(n1, expected, actual))
    #     # else:
    #     #     print(actual)