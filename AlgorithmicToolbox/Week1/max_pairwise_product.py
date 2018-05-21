# Uses python3
# First line has integer for number of ints in subsequent array
# Second line has array of integers
# Return the maximum pairwise product of two non-same members of the array (may share values)
n = int(input())
intArray = [int(x) for x in input().split()]
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
print(result)
