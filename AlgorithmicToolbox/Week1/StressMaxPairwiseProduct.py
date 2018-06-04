# Uses python3

import sys
import random
from array import array
import max_pairwise_product_Naive
import max_pairwise_product

MAX_NUMBERS = 10
MAX_VALUE = 100000
while True:
    n = random.randint(2,MAX_NUMBERS)
    print(n)
    a = []

    for i in range(0, n):
        a.append(int(random.randint(0,MAX_VALUE)))
        print(a[i], end=" ")
    print()

    intArray = array("i", a)
    res1 = max_pairwise_product_Naive.MaxPairwiseProductNaive(n, intArray)
    res2 = max_pairwise_product.MaxPairwiseProductFast(n, intArray)
    if res1 == res2:            
        print("OK")        
    else:            
        print("Wrong answer: {}, {}".format(res1, res2))    
        break