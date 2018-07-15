# Uses python3
import sys

def get_change(m):
    denominations = [10,5,1]
    count = 0
    while(m >= min(denominations)):
        count += 1
        for d in denominations:
            if(m >= d):
                m -= d
                break

    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    # m = int(input())
    print(get_change(m))
