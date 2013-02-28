##Factorial digit sum
##Problem 20
##n! means n  (n  1)  ...  3  2  1
##
##For example, 10! = 10  9  ...  3  2  1 = 3628800,
##and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
##
##Find the sum of the digits in the number 100!



def facto(digit):
    total = 1
    while digit > 0:
        total *= digit
        digit -= 1
    print total
    sumdig = 0
    #total = str(total)
    for dig in str(total):
        sumdig += int(dig)
    return sumdig
        


print facto(100)



##import math as m
##print sum([int(i) for i in str(m.factorial(100))])


##from math import factorial as f
##
##def problem20():
##    return sum([int(x) for x in str(f(100))])
##
##def somPro():
##    pro = 1
##    for i in range(1, 101):
##        pro *= i
##    return sum(j for j in list(int(i) for i in str(pro)))
##
##print(somPro())
