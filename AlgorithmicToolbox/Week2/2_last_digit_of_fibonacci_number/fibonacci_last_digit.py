# Uses python3
# Calculate the last digit of the nth fibonacci number
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        #note, this is using tuples to perform a destructuring assignment.
        #equivalent to previous = current and current = previous + current.
        #"assign previous and current equal to current and (previous + current) respectively"
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current % 10, (previous + current)%10

    return current % 10

if __name__ == '__main__':
    n = int(input())
    # for n1 in range(n):
    #     if get_fibonacci_last_digit_naive(n1) != get_fibonacci_last_digit(n1):
    #         print("Wrong answer: n={}, expected:{}, actual:{}".format(n1, get_fibonacci_last_digit_naive(n1), get_fibonacci_last_digit(n1)))

    print(get_fibonacci_last_digit(n))
