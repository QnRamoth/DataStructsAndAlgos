# Uses python3
# These functions report the n-th Fibonacci number modulus m
# The pisano period is the number of Fibonacci values before a given modulus m begins to repeat.
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    pisano_period = get_pisano_period(m)
    equivalent_n = n % pisano_period

    previous = 0
    current  = 1

    for _ in range(equivalent_n - 1):
        previous, current = current, previous + current

    return current % m


def get_pisano_period(m):
    previous = 0
    current = 1
    fibModulusArray = [previous%m]

    for i in range(m**2+3):
        previous, current = current, previous + current
        fibModulusArray.append(previous%m)
        if(
            i>3 and 
            fibModulusArray[-3] == 0 and 
            fibModulusArray[-2] == 1 and 
            fibModulusArray[-1] == 1):
            return i-1

if __name__ == '__main__':
    inputs = input()
    n, m = map(int, inputs.split())
    # print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge(n, m))
