# Uses python3
# Understand Greatest Common Divisor as the greatest integer that divides two non-negative integers
# Lemma: Let a' be the remainder when a is divided by b: 
# gcd(a,b)=gcd(a',b)=gcd(b,a')
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd(a, b):
    a, b = max(a,b), min(a,b)
    while b !=0:
        a, b = b, a%b
    return a

# input expects two non-negative integers separated by a space
if __name__ == "__main__":
    inputs = input()
    a, b = map(int, inputs.split())
    # print(gcd_naive(a, b))
    print(gcd(a,b))
