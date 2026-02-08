minnb, maxnb, nb, som = 1000, 0, 0, 0  # initializations

while 1:  # repeat input until user enters 0
    try:
        val = int(input("Three-digit number or 0 to stop: "))
    except:continue
    if val == 0:break
    elif val in range(100, 1000):
        nb += 1       # count the entered number
        som += val    # accumulate the sum of numbers
        if maxnb < val:
            maxnb = val   # update maximum
        if minnb > val:
            minnb = val   # update minimum
        break
print("Maximum={} Minimum={} Average={:.3f}".format(maxnb, minnb, som/nb))
for nb in range(minnb, maxnb + 1):  # display Keith numbers between minnb and maxnb
    # test if nb is a Keith number to display it
    U0, U1, U2 = nb // 100, (nb % 100) // 10, nb % 10  # initialize the sequence terms
    print(U0, U1, U2, end='  ')#print first three terms

    while 1:  # repeat calculation of U3 until reaching or exceeding nb
        U3 = U0 + U1 + U2
        if U3 < nb:
            print(U3, end= ' ')
            # update the sequence terms
            U0, U1, U2 = U1, U2, U3
        elif U3 == nb:  # nb is a Keith number, display it and stop
            print(U3)
            break
        else:  # U3 > nb, stop
            break
