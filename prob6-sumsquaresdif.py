##The sum of the squares of the first ten natural numbers is,
##
##12 + 22 + ... + 102 = 385
##The square of the sum of the first ten natural numbers is,
##
##(1 + 2 + ... + 10)2 = 552 = 3025
##Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
##
##Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
##

square = 1
mtotal = 0

for i in range(1,11):
    stotal = square * square
    #stotal = square^2
    mtotal += stotal
    square += 1

qtotal = 0
mqtotal = 0

for i in range(1,11):
    qtotal += i
    mqtotal = qtotal * qtotal
    #mqtotal = qtotal^2


print mqtotal
print mtotal

answer = mqtotal - mtotal
print answer


##print pow((1+100)*100/2, 2) - sum(x*x for x in xrange(1, 101))
    

##def sum_of_the_squares(n):
##   ''' returns 1^2 + 2^2 + 3^2 + 4^2 + ... + n^2'''
##
##   return sum(x**2 for x in xrange(1,n+1))
##
##def square_of_the_sum(n):
##   ''' returns (1+2+3+4+...+n)^2'''
##
##   return sum(xrange(1,n+1))**2
##
##print(square_of_the_sum(100) - sum_of_the_squares(100))
