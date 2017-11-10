# def gemmidelde(zin):
#     list = []
#     zin = zin.split()
#     for woord in zin:
#         list.append(len(woord))
#
#     # return sum(zin) / len(zin)
# zin = input('Geef een zin: ')
# gemmidelde(zin)
# print('gemiddelde: ' + str(gemmidelde(zin)))
# print(list)

# zin in int krijgen maar weet niet hoe

def gemiddelde(zin):
    woorden = zin.split()
    aantal = sum(len(woord)for woord in woorden) / len(woorden)
    print('Het gemiddelde letter per woord in die zin is:',aantal)
    return gemiddelde
zin = input('Geef een willekeurige zin: ')
gemiddelde(zin)