# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    weight = 0.
    valueDensities = []
    for i in range(len(weights)):
        valueDensities.append(values[i] / weights[i])
    loot = sorted(zip(valueDensities, weights, values))

    while (weight<capacity and len(loot)>0):
        item = loot.pop()
        if(capacity-weight > item[1]):
            weight += item[1]
            value += item[2]
        else:
            value += (capacity-weight)*item[0]
            weight = capacity

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    # data = list(map(int, input().split()))
    n, capacity = data[0:2] #assign first to values to n and capacity
    values = data[2:(2 * n + 2):2] #assign every other value from 2 to 2*n+2
    weights = data[3:(2 * n + 2):2] #assign every other value from 3 to 2*n+2
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
