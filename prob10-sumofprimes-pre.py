##
##Problem 7
##By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
##
##What is the 10 001st prime number?
##


def primes(limit):
    
    not_prime = [False] * limit
    primes = []
    
    for n in range(2, limit):
        if not_prime[n]:
            continue
        for f in xrange(n*2, limit, n):
            not_prime[f] = True
        primes.append(n)
        
    return primes

generate = primes(2000000)
print sum(generate)

# 142913828922

##
##def primes(limit):
##    limitn = limit + 1
##    not_prime = [False] * limitn
##    primes = []
##    for n in range(2, limitn):
##        if not_prime[n]:
##            continue
##        for f in xrange(n*2, limitn, n):
##            not_prime[f] = True
##        primes.append(n)
##    return primes
##generate = primes(2000000)
##print sum(generate)









##n = 0
##
##def trial_division(n):
##    """Return a list of the prime factors for a natural number."""
##    if n == 1: return [1]
##    primes = prime_sieve(int(n**0.5) + 1)
##    prime_factors = []
## 
##    for p in primes:
##        if p*p > n: break
##        while n % p == 0:
##            prime_factors.append(p)
##            n //= p
##    if n > 1: prime_factors.append(n)
## 
##    return prime_factors
##
##for i in range(1,10):
##    print trial_division(i)
##
##import math
##
##def get_prime(target):
##    primes = [2]
##    count = 1
##    num = 1
##    while count < target:
##        num += 2
##        is_prime = True
##        for prime in primes:
##            if prime > math.sqrt(num): break #speeds up calculation hugely
##            if not num % prime:
##                is_prime = False
##                break
##        if is_prime:
##            primes.append(num)
##            count += 1
##   return num


##def isPrime(n):
##    for i in range(2, n):
##        if n%i==0:
##            return False
##    print n
##    return True
##
##num = 3
##primesum = 0
##
##while True:
##    if isPrime(num):
##        primesum += num
##    if num > 2000000:
##        break
##    num+=1
##
##print primesum + 3




##def is_prime(x):
##   if x < 2:
##      return False
##   for i in range(2, x-1):
##      if x % i == 0:
##         return False
##   return True
##   
##primecount = 1
##i = 1
##while primecount < 10002:
##   if is_prime(i) == True:
##      print(str(i) + " is the " + str(primecount) + " numbered prime.")
##      primecount += 1
##   i += 1


##import math

##def get_prime(target):
##    primes = [2]
##    count = 1
##    num = 1
##    while count < target:
##        num += 2
##        is_prime = True
##        for prime in primes:
##            if prime > math.sqrt(num): break #speeds up calculation hugely
##            if not num % prime:
##                is_prime = False
##                break
##        if is_prime:
##            primes.append(num)
##            count += 1
##    return num
##
##print get_prime(10001)
###

##import math
##
##
##primes = [2]
##count = 1
##num = 1
##primesum = 0
##
##while primes < 2000000:
##    num += 1
##    for prime in primes:
##        if prime > math.sqrt(num): break #speeds up calculation hugely
##    primesum += prime
##        
##print num
##print primesum
##
##



##from math import *
##
##def prime(num):
##   top = int(sqrt(num)) + 1
##   for i in range(1, top):
##      if((num%i == 0) and (i > 1)):
##         return False
##   return True
##
##count = 0
##for i in range(2, 10001**2):
##   if(prime(i)):
##      count += 1
##
##      if(count == 10001):
##         print(i)
##         exit()
##
##


##import math
##
##def isPrime(a):
##    b = int(math.sqrt(a)) + 1
##    for i in xrange(2,b):
##        if (a % i) == 0:
##            return False
##    return True
##
##i = 1
##n = 0
##primesum = 0
##
##while primesum < 2000000:
##    i += 1
##    n += isPrime(i)
##    primesum += 
##    
##print i
##print primesum
##
