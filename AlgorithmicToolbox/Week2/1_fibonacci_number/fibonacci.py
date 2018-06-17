# Uses python3
# Understand Fibonacci sequence as F[0]==0, F[1]==1, and F[i]==F[i-1]+F[i-2]
def calc_fib_naive(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_array(n):
    assert(n >= 0)
    if (n <= 1):
        return n

    fibArray = []
    for i in range(n+1):
        if (i <= 1):
            fibArray.append(i)
        else:
            fibArray.append(fibArray[i-1] + fibArray[i-2])
    return fibArray[-1]

def calc_fib(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n-1):
        previous, current = current, previous + current
    return current

if __name__=="__main__":
    n = int(input())
    # print(calc_fib_naive(n))
    # print(calc_fib_array(n))
    print(calc_fib(n))

    # for n1 in range(2,10000):
    #     print(calc_fib_naive(n1))
    #     print(calc_fib_array(n1))
    #     print(calc_fib(n1))
