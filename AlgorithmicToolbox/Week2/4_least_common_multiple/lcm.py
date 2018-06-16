# Uses python3
# Understand Least Common Multiple as the least positive integer 
# divisible by two integers.
# Note that lcm(a,b)=abs(a*b)/gcd(a,b)
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm(a, b):
    return int((abs(a)/gcd(a,b))*abs(b))

def gcd(a, b):
    a, b = max(a,b), min(a,b)
    while b !=0:
        a, b = b, a%b
    return a

if __name__ == '__main__':
    inputs = input()
    a, b = map(int, inputs.split())
    #print(lcm_naive(a, b))
    print(lcm(a,b))
