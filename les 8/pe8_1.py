bruin = {'Boxtel','best','beukenlaan','Eindhoven','Helmond','t Hout','Helmond','Helmond Brouwhuis','Deurne'}
groen = {'Boxtel','best','beukenlaan','Eindhoven','Geldrop','Heeze','Weert'}
def overeenkomst():
    station = groen.intersection(bruin)
    print(station)
def verschillen():
    station2 = groen.difference(bruin)
    print(station2)
def alles():
    station3 = groen.union(bruin)
    print(station3)
overeenkomst()
verschillen()
alles()