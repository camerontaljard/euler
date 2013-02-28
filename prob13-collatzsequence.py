

answer = 0
count = 0
bign = 0
bignn = 0
bigc = 0


for number in range(3,999999):
    #print 'Start: ', number
    bignn = number

    while number != 1:
        count += 1
    
        if number % 2 == 0:
            answer = number / 2
            #print answer
            #break
    
        elif number % 2 != 0:
            answer = 3 * number + 1
            #print answer
            #break

        #print answer
            
        number = answer

    if count > bigc:
        bigc = count
        bign = bignn
        
    #print 'count: ', count
    
    count = 0

print bigc, bign




##import time
##
### Brute force method
##def CL(n):
##   length = 1
##   m = n
##   while m != 1:
##      if m % 2 == 0: #is even
##         m = m / 2
##      else:
##         m = 3*m + 1
##      length = length +  1
##      # end if/else
##   # end while
##   return length
##
### Dynamic programming method
##CacheMax = 1000000
##cached = [None] * CacheMax
##cached[1] = 1
##def recCL(n):
##   if n < CacheMax and cached[n] != None:
##      return cached[n]
##   elif n % 2 == 0:
##      temp = 1 + recCL(n/2)
##   else:
##      temp = 1 + recCL(3*n+1)
##   if n < CacheMax:
##      cached[n] = temp
##   return temp
##
### Brute force method takes about 34 seconds
### Dynamic programming method takes ~2 seconds
##start = time.clock()
##maxLen = 0
##maxInd = None
##for ii in range(1, 1000000):
##   a = recCL(ii)
##   if a > maxLen:
##      maxLen = a
##      maxInd = ii
##end = time.clock()
##print "Elapsed =", end-start
##print maxInd
