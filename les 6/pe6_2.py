# for woord in lijst:
#     newlijst = len(lst) == 4
#     print('De nieuwe-gemaakte lijst met alle vier-letter strings is: '+newlijst)
# lijst = eval(input('geef lijst met minimaal 10 strings: '))

def zin():
    lst = []
    nieuw = input('Geef een zin van 10 karakters: ')
    nieuw = nieuw.split(' ')
    for woord in nieuw:
        lengte = len(woord)
        if lengte == 4:
            lst.append(woord)
    print(lst)
zin()