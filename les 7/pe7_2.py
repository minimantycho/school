while True:
    woord = input('Geef een woord van 4 letters: ')
    lengte = len(woord)
    zin = str(lengte)
    if lengte == 4:
        print('In lezen van ' + woord + ' is gelukt')
        break

    else:
        fout = str(woord + ' heeft ' + zin + ' letters')
        print(fout)


