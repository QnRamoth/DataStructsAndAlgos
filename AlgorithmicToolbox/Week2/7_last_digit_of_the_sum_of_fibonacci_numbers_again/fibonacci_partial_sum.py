# Uses python3
# Calculates the last digit of the partial sum of fibonacci numbers from the mth to the nth.
# Note that the sum of this range is equal to F(n+2) - F(m+1) - 2
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def fibonacci_partial_sum(from_, to):
    assert(to >= from_)

    fib_mPlusOneLastDigit = get_fibonacci_huge_last_digit(from_+1)-1
    fib_nPlusTwoLastDigit = get_fibonacci_huge_last_digit(to+2)-1
    difference = fib_nPlusTwoLastDigit - fib_mPlusOneLastDigit

    if(difference < 0):
        difference += 10

    return difference

def get_fibonacci_huge_last_digit(n):
    pisano_period = 60
    equivalent_n = n % pisano_period

    if equivalent_n <= 1:
        return equivalent_n


    previous = 0
    current  = 1

    for _ in range(equivalent_n - 1):
        previous, current = current, previous + current

    return current % 10


if __name__ == '__main__':
    inputs = input()
    m, n = map(int, inputs.split())
    # print(fibonacci_partial_sum_naive(m, n))
    print(fibonacci_partial_sum(m, n))

    # for n1 in range(m,n+1):
    #     expected = fibonacci_partial_sum_naive(m, n1)
    #     actual = fibonacci_partial_sum(m, n1)
    #     if actual != expected:
    #         print("Wrong answer: n={}, expected:{}, actual:{}".format(n1, expected, actual))
    #     # else:
    #     #     print(actual)