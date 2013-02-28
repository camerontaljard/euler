numfile = open('product.txt', 'w')

print numfile

psum = 0

yside = 100
xside = 100

for y in range(100,999):
    yside += 1
    for x in range(100, 999):
        psum = yside * x 
        #print psum
        numfile.write(str(psum))
        numfile.write('\n')

numfile = open('product.txt', 'r')

larpal = 0

for y in numfile:
    b1 = y[0:1]
    b2 = y[1:2]
    b3 = y[2:3]
    
    hl = len(y)
    
    e1 = y[hl-2:]
    e2 = y[hl-3:hl-2]
    e3 = y[hl-4:hl-3]
    
    if int(b1) == int(e1) and int(b2) == int(e2) and int(b3) == int(e3):
        #print y
        if int(y) > int(larpal):
            larpal = y
            
   
print larpal
print 'Done'
