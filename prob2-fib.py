
#fibinacci sequence, add evens

a = 0

b = 1

count = int(0)

addit = int(0)

#while count < 100:
#while count < 32:

while True:
    count = count + 1
    a, b = b, a + b
    #print count, a
    #if a >= 4000000:
    if len(str(a)) == 1000:
        print count
        break
    if a % 2 == 0:
        addit = addit + int(a)

        
print 'Sum: ', addit


    
#thet way it should be done
##a,b,c=1,2,0
##while b < 4000000:
##    c+=b
##    a,b=a+b+b,a+a+b+b+b
##print c

##quicker way
##x = 1
##y = 2
##n = 0
##a = 2
##while n <= 4000000:
##    n = x + y
##    if n%2 == 0:
##        a = a + n
##        print (a)
## x = y
