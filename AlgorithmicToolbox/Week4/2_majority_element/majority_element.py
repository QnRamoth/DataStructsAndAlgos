# Uses python3
import math
import sys


def get_majority_element_naive(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    for val in a:
        count = 0
        for scanValue in a:
            if scanValue == val:
                count += 1
        if count > len(a)/2:
            return val
    return -1


def get_majority_element(a, left, right):
    if left == right:
        return a[left]
    elif left + 1 == right:
        if a[left] == a[right]:
            return a[left]
        else:
            return -1
    elif left + 2 == right:
        if (a[left] == a[right]) or (a[left] == a[left+1]):
            return a[left]
        elif a[left+1] == a[right]:
            return a[right]
        else:
            return -1

    midpoint = math.floor((left + right)/2)
    leftMajority = get_majority_element(a, left, midpoint)
    rightMajority = get_majority_element(a, midpoint+1, right)

    if leftMajority == -1 and rightMajority >= 0:
        return rightMajority
    elif rightMajority == -1 and leftMajority >= 0:
        return leftMajority
    elif leftMajority == rightMajority:
        return leftMajority
    else:
        return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element_naive(a, 0, n) != -1:
        print(1)
    else:
        print(0)

    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)
