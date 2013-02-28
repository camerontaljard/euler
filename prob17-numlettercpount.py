##Number letter counts
##Problem 17
##If the numbers 1 to 5 are written out in words: one, two, three, four, five,
##then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
##
##If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
##
##
##NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
##and 115 (one hundred and fifteen)
##contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

biglist = []

single = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

double = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

mylist = []

trip = ['hundredand']

dcount = 9

count = -1



while True:
    count = count + 1
    for numb in single:
        new = double[count] + numb
        print new 
        mylist.append(new)



print mylist
    
##
##for d,s in zip(double, single):
##    print d + s

    

##for it in double:
##    #new = double[dcount] + single[ccount]
##    #ccount = ccount + 1
##    while dcount > 0:
##        dcount = dcount + 1
##        new = double[dcount] + single[ccount]
##        dcount = dcount + 1
##        print new
##        


##for b, a in zip(double, single):
##    
##    print b, a
    #new = b + single[ccount]
    #ccount = ccount + 1
    #print new
    
    

