# -*- coding: utf-8 -*-
##Problem 3
##The prime factors of 13195 are 5, 7, 13 and 29.
##
##What is the largest prime factor of the number 600851475143 ?




##def gcd (a, b):
##    if a == 0:
##        return b
##    while b != 0:
##        if a > b:
##            a == a- b
##        else:
##            b == b - a
##        return a
##
##print gcd(0,600851475143)



##def lpf(a,b):
##    while b != 0:
##        t = b
##        b = a % t
##        a = t
##    return a
##
##print lpf(1071,462)
##
##
##def gcd(a, b):
##    if a == 0:
##       return b
##    while b != 0:
##        if a > b:
##           a = a - b
##        else:
##           b = b - a
##    return a
##
##print gcd(1071,462)
##
##
##
##def lpf2(a,b):
##    if b == 0:
##        return a
##    else:
##        return lpf2(b, a % b)
##
##print lpf2 (1071,462)



##def prime_factors(n):
##    "Returns all the prime factors of a positive integer"
##    factors = []
##    d = 2
##    while (n > 1):
##        while (n%d==0):
##            factors.append(d)
##            n /= d
##        d = d + 1
##        if (d*d>n):
##            if (n>1): factors.append(n);
##            print factors
##            break;
##    return factors
##
##
##
##pfs = prime_factors(600851475143)
##print pfs[-1] # The largest (last) element in the prime factor array



def largestprime(thenumber):
    factors = []
    divisor = 2
    while (thenumber > 1):
        
        while (thenumber % divisor == 0):
            factors.append(divisor)
            thenumber /= divisor
            
        divisor = divisor + 1
        
        if (divisor * divisor > thenumber):
            if (thenumber > 1): factors.append(thenumber);
            print factors
            break;
    return factors


x = largestprime(13195)
 
print x[-1]




 
        

