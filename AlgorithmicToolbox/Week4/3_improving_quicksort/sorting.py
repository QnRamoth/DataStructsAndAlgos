# Uses python3
import sys
import random


def partition3(a, left, right):
    m1 = left
    m2 = right

    x = a[left]

    i = left + 1
    while i <= m2:
        if a[i] < x:
            a[i], a[m1] = a[m1], a[i]
            m1 += 1
            i += 1
        elif a[i] > x:
            a[i], a[m2] = a[m2], a[i]
            m2 -= 1
        elif a[i] == x:
            i += 1

    return m1, m2


def partition2(a, left, right):
    x = a[left]
    j = left
    for i in range(left + 1, right + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[left], a[j] = a[j], a[left]
    return j


def randomized_quick_sort(a, left, right):
    if left >= right:
        return
    k = random.randint(left, right)
    a[left], a[k] = a[k], a[left]

    m = partition2(a, left, right)
    randomized_quick_sort(a, left, m - 1)
    randomized_quick_sort(a, m + 1, right)


def randomized_quick_sort3(a, left, right):
    if left >= right:
        return
    k = random.randint(left, right)
    a[left], a[k] = a[k], a[left]

    m = partition3(a, left, right)
    randomized_quick_sort3(a, left, m[0] - 1)
    randomized_quick_sort3(a, m[1] + 1, right)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # b = a.copy()
    # randomized_quick_sort(b, 0, n - 1)
    # for x in b:
    #     print(x, end=' ')
    # print('')

    randomized_quick_sort3(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
