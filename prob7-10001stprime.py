##10001st prime
##Problem 7
##By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
##
##What is the 10 001st prime number?
##
##n = 0
##
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
##for i in range(1,10):
##    print trial_division(i)


def isPrime(n):
    for i in range(2, n):
        if n%i==0:
            return False
    print n
    return True

cnt = 1
num = 3
while True:
    if isPrime(num):
        cnt+=1
    if cnt>10000:
        break
    num+=1
print num



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
