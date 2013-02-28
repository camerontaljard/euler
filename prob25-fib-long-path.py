

a = 0
b = 1
term = int(0)

while True:
    term += 1
    a, b = b, a + b
    if len(str(a)) == 1000:
        print term
        break

