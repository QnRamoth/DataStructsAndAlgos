# Uses python3
def MaxPairwiseProductNaive(n, intArray):
    assert(len(intArray) == n)

    result = 0

    for i in range(0, n):
        for j in range(i+1, n):
            if intArray[i]*intArray[j] > result:
                result = intArray[i]*intArray[j]

    return result
    
if __name__=="__main__":
    n = int(input())
    a = input()
    intArray = [int(x) for x in a.split()]

    result = MaxPairwiseProductNaive(n, intArray)

    print(result)
