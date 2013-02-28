##Smallest multiple
##Problem 5
##2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
##What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

number = 1000000000
magicnumber = 0

while number > 0:
    number -= 1
    #print number
    if number % 1 == 0:
        #print number
        if number % 2 == 0:
            #print number
            if number % 3 == 0:
                #print number
                if number % 4 == 0:
                    #print number
                    if number % 5 == 0:
                        #print number
                        if number % 6 == 0:
                            #print number
                            if number % 7 == 0:
                                #print number
                                if number % 8 == 0:
                                    #print number
                                    if number % 9 == 0:
                                        #print number
                                        if number % 10 == 0:
                                            #print number
                                            if number % 11 == 0:
                                                #print number
                                                if number % 12 == 0:
                                                    #print number
                                                    if number % 13 == 0:
                                                        #print number
                                                        if number % 14 == 0:
                                                            #print number
                                                            if number % 15 == 0:
                                                                #print number
                                                                if number % 16 == 0:
                                                                    #print number
                                                                    if number % 17 == 0:
                                                                        #print number
                                                                        if number % 18 == 0:
                                                                            #print number
                                                                            if number % 19 == 0:
                                                                                #print number
                                                                                if number % 20 == 0:
                                                                                    print number
                                                                                    
                                                                        
##
##def gcd(a, b):
##    while b != 0:
##        a, b = b, a % b
##    return a
##
##def lcm(a, b):
##    return a*b/gcd(a, b)
##
##print reduce(lcm, range(1, 20+1))
