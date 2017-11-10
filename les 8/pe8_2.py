import random

doubleCount = 0
def monopolyworp():
    global doubleCount
    while True:
        dobbel1 = int(random.randrange(1,7))
        dobbel2 = int(random.randrange(1,7))
        som = (dobbel1 + dobbel2)
        print(dobbel1, '+', dobbel2, '=', som)
        if dobbel1 == dobbel2:
            dubbel = print(str(dobbel1), ' + ', str(dobbel2), ' = ', str(som), 'dubbel')
            doubleCount += 1
            if doubleCount == 3:
                print('Je gaat naar de gevangenis')
                break



        print('')
monopolyworp()