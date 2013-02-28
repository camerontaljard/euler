#233168

count = int(1000)

numlist = list()

while count != 0:
    count = count  - 1
    numlist.append(count)

inlist = list()
outlist = list()
    
for number in numlist:
    number = int(number)
    if number % 3 == 0:
        if number not in inlist:
            inlist.append(number)
    else:
        if number not in outlist:
            outlist.append(number)
    if number % 5 == 0 :
        if number not in inlist:
            inlist.append(number)
    else:
        if number not in outlist:
            outlist.append(number)

outtotal = int(0)
intotal = int(0)

for x in outlist:
    outtotal = x + outtotal


for y in inlist:
    intotal = y + intotal


print outtotal
print intotal

#print total    
#print numlist
#print number
#print outlist
#print inlist
