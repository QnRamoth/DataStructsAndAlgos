# Uses python3
# First line has integer for number of ints in subsequent array
# Second line has array of integers
# Return the maximum pairwise product of two non-same members of the array (may share values)
def MaxPairwiseProductFast(n, intArray):
    assert(len(intArray) == n)

    maxValue = max(intArray[0],intArray[1])
    nextMaxValue = min(intArray[0],intArray[1])

    for i in range(2,n):
        if intArray[i] > maxValue:
            nextMaxValue = maxValue
            maxValue = intArray[i]
        elif intArray[i] > nextMaxValue:
            nextMaxValue = intArray[i]

    result = maxValue*nextMaxValue

    #print(maxValue)
    #print(nextMaxValue)
    return result

if __name__=="__main__":
    n = int(input())
    a = input()
    intArray = [int(x) for x in a.split()]

    result = MaxPairwiseProductFast(n, intArray)

    print(result)