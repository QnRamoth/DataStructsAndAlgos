# Uses python3
import sys


def merge(b, a, left, mid, right):
    i = left
    j = mid
    inversion_count = 0
    for k in range(left, right):
        if i < mid and (j >= right or a[i] <= a[j]):
            b[k] = a[i]
            i += 1
        else:
            if a[i] > a[j]:
                inversion_count += (mid - i)
            b[k] = a[j]
            j += 1
    return inversion_count


def get_number_of_inversions(a, b, left, right):
    if left == 0 and right == len(a):
        b = a.copy()
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    mid = (left + right) // 2
    number_of_inversions += get_number_of_inversions(b, a, left, mid)
    number_of_inversions += get_number_of_inversions(b, a, mid, right)

    number_of_inversions += merge(a, b, left, mid, right)

    return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
    # print(a)
    # print(b)
