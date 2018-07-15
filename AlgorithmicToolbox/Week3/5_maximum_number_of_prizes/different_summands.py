# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    remainder = n
    lastPrize = 0
    while (remainder > 0):
        if(remainder > 2*(lastPrize + 1)):
            summands.append(lastPrize + 1)
        else:
            summands.append(remainder)
        lastPrize = summands[-1]
        remainder -= lastPrize

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
