#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    while(len(a) > 0):
        maxDigit = a[0]
        for digit in a:
            if(isGreaterOrEqual(digit, maxDigit)):
                maxDigit = int(digit)
        res += str(maxDigit)
        a.pop(a.index(str(maxDigit)))
    return res

def isGreaterOrEqual(digit, maxDigit):
    d_md = int(str(digit) + str(maxDigit))
    md_d = int(str(maxDigit) + str(digit))
    return d_md >= md_d

if __name__ == '__main__':
    inputs = input()
    data = inputs.split()
    a = data[1:]
    print(largest_number(a))
    
