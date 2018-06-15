# Uses python3
# Understand Fibonacci sequence as F[0]==1, F[1]==1, and F[i]==F[i-1]+F[i-2]
def calc_fib_naive(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib(n):
    assert(n >= 0)

    fibArray = []
    for i in range(n):
        if (i <= 1):
            fibArray.append(i)
        else:
            fibArray.append(fibArray[i-1] + fibArray[i-2])
    return fibArray[-1]

if __name__=="__main__":
    n = int(input())
    #print(calc_fib_naive(n))
    print(calc_fib(n))
